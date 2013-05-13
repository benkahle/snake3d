import socket
import select as sel
import random
import time
import re
from visual import *

class SnakeClient(object):
  def __init__(self, addr="192.168.172.144", serverport=55556):
    self.clientport = random.randint(8000, 8999)
    self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.addr = addr
    self.serverport = serverport
    self.read_list = [self.conn]
    self.write_list = []
    
    self.setup_game()
  
  def setup_game(self):
    #Setup vpython game world here
    self.scene = display(title='Super-Mega Snake Game', width=750, height=775)
    self.welcome = label(text='Welcome to Super-Mega Snake Game!',align='center',pos=(0,0,0), yoffset= 60, height = 25)
    self.welcome_purple = label(text = 'When both players are ready, use arrow keys to control movement of snake. \nThe snake dies if it hits the wall, itself or the other snake. \nWin by staying alive.',pos=(0,0,0), color = color.magenta, align = 'center')
    self.border = curve(pos=[(-100,-100),(100,-100),(100,100),(-100,100),(-100,-100)])
    self.scene.autoscale = False
    #self.snake = box(pos=(0,0,0), length=4, width=4, height=4, color=color.red)
    self.p1_boxes = []
    self.p2_boxes = []
    self.food_box = box(pos=(100,100),length=4,width=4,height=4,color=color.cyan)

  def make_snake(self,coords,player):
    if player == 'p1':
      if len(coords) > len(self.p1_boxes):
        item = box(pos=coords[-1],length=3,width=3,height=3,color=color.red)
        self.p1_boxes.append(item)
      for snake_box in self.p1_boxes:
        snake_box.pos = coords[-(self.p1_boxes.index(snake_box))]
    if player == 'p2': 
      if len(coords) > len(self.p2_boxes):
        item = box(pos=coords[-1],length=3,width=3,height=3,color=color.green)
        self.p2_boxes.append(item)
      for snake_box in self.p2_boxes:
        snake_box.pos = coords[-(self.p2_boxes.index(snake_box))]

  def run(self):
    running = True
    time.sleep(.1)
    # Initialize connection to server
    self.conn.sendto("c", (self.addr, self.serverport))
    # localip, localport = self.conn.getsockname()
    # print(localip,localport)
    while running:
      # select on specified file descriptors
      readable, writable, exceptional=(sel.select(self.read_list, self.write_list, [],0.1))
      for f in readable:
        if f is self.conn: #if a packet is received
          msg, sentaddr = f.recvfrom(4096)
          #print(msg,sentaddr)
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
          if running_state == 'True':
            pass
          # elif running_state == str(localport):
          #   print(running_state)
          #   print('and you are')
          #   print(localport)
          #   loss_text = label(text='You Lose!', align='center',pos=[0,0],height=30,color=color.red)
          #   running = False
          else:
            loss_text = label(text='Game Over!', align='center',pos=[0,0],height=30,color=color.red)
            running = False
          # except:
          #   pass  # If something goes wrong, don't draw anything.
      if self.scene.kb.keys:
        self.welcome.visible = False
        self.welcome_purple.visible = False
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