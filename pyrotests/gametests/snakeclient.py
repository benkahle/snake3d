import socket
import select as sel
import random
import time
import re
from visual import *

class SnakeClient(object):
  def __init__(self, addr="10.41.64.143", serverport=9007):
    self.clientport = random.randint(8000, 8999)
    self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind to localhost - set to external ip to connect from other computers
    # self.conn.bind(("127.0.0.1", self.clientport))
    self.addr = addr
    self.serverport = serverport
    self.read_list = [self.conn]
    self.write_list = []
    
    self.setup_game()
  
  def setup_game(self):
    #Setup vpython game world here
    self.scene = display(title='Super-Mega Snake Game', width=250, height=250)
    self.border = curve(pos=[(-100,-100),(100,-100),(100,100),(-100,100),(-100,-100)])
    self.scene.autoscale = False
    #self.snake = box(pos=(0,0,0), length=4, width=4, height=4, color=color.red)
    self.p1_boxes = []
    self.p2_boxes = []
    self.food_box = box(pos=(100,100),length=4,width=4,height=4,color=color.cyan)

  def check_keyinput(self):
    cmd = ' '
    check = True
    while check:
      #if self.scene.kb.keys: # is there an evcd UnicodeDecodeError()ent waiting to be processed?
        # welcome.visible=0
        # welcomebox.visible=0
        key = self.scene.kb.getkey() # obtain keyboard information
        if key == 'left':
          cmd = 'a'
          check = False
        if key == 'right':
          cmd = 'b'
          check = False
        if key == 'up':
          cmd = 'c'
          check = False
        if key == 'down':
          cmd = 'd'
          check = False
        # if key == 's':
        #   cmd = 'e'
        #check = False
        # if key == 'w': 
        #   cmd = 'f'
        #check = False
        if key == 'q':
          cmd = 'quit'
    return cmd

  def make_snake(self,coords,player):
    if player == 'p1':
      if len(coords) > len(self.p1_boxes):
        item = box(pos=coords[-1],length=4,width=4,height=4,color=color.red)
        self.p1_boxes.append(item)
      for snake_box in self.p1_boxes:
        snake_box.pos = coords[-(self.p1_boxes.index(snake_box))]
    if player == 'p2': 
      if len(coords) > len(self.p2_boxes):
        item = box(pos=coords[-1],length=4,width=4,height=4,color=color.green)
        self.p2_boxes.append(item)
      for snake_box in self.p2_boxes:
        snake_box.pos = coords[-(self.p2_boxes.index(snake_box))]

  def run(self):
    running = True

    try:
      time.sleep(.1)
      # Initialize connection to server
      self.conn.sendto("c", (self.addr, self.serverport))
      while running:
        #'Wait' function for discrete time?
        
        # select on specified file descriptors
        readable, writable, exceptional=(sel.select(self.read_list, self.write_list, [],0.1))
        for f in readable:
          if f is self.conn: #if a packet is received
            msg, sentaddr = f.recvfrom(4096)
            print(msg,sentaddr)
            messages = []
            for inner_message in msg.split('|'):
              messages.append(inner_message)
            p1_coords = []
            p2_coords = []
            for position in messages[0].split(';'): #snake '1'
              position = re.sub('[\(\)]','',position)
              positions = []
              for i in position.split(','):
                positions.append(i)
              p1_coords.append(vector(int(positions[0]),int(positions[1])))
            for position in messages[1].split(';'): #snake '2'
              position = re.sub('[\(\)]','',position)
              positions = []
              for i in position.split(','):
                positions.append(i)
              p2_coords.append(vector(int(positions[0]),int(positions[1])))
            self.make_snake(p1_coords,'p1')
            self.make_snake(p2_coords,'p2')
            position = messages[2] #food
            position = re.sub('[\(\)]','',position)
            positions = []
            for i in position.split(','):
              positions.append(i)
            #print(positions)
            self.food_box.pos = vector(int(positions[0]),int(positions[1]))
            running_state = messages[3]
            if running_state == 'run':
              pass
            elif running_state == self.clientport:
              loss_text = label(text='You Lose!', align='center',pos=[0,0],height=30,color=color.red)
              running = False
            else:
              loss_text = label(text='You Win!', align='center',pos=[0,0],height=30,color=color.red)
              running = False
            # except:
            #   pass  # If something goes wrong, don't draw anything.
        if self.scene.kb.keys:
          key = self.scene.kb.getkey()
          if key == 'left':
            self.conn.sendto('ua',(self.addr, self.serverport))
          if key == 'right':
            self.conn.sendto('ub',(self.addr, self.serverport))
          if key == 'up':
            self.conn.sendto('uc',(self.addr, self.serverport))
          if key == 'down':
            self.conn.sendto('ud',(self.addr, self.serverport))
          if key == 'q':
            running = False
        self.conn.sendto("d", (self.addr, self.serverport))


if __name__ == "__main__":
  g = SnakeClient()
  g.run()