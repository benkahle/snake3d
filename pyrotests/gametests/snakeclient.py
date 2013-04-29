import socket
import select as sel
import random
import time
from visual import *

class SnakeClient(object):
  def __init__(self, addr="127.0.0.1", serverport=9007):
    self.clientport = random.randint(8000, 8999)
    self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind to localhost - set to external ip to connect from other computers
    self.conn.bind(("127.0.0.1", self.clientport))
    self.addr = addr
    self.serverport = serverport
    self.read_list = [self.conn]
    self.write_list = []
    
    self.setup_game()
  
  def setup_game(self):
    #Setup vpython game world here
    self.scene = display(title='Super-Mega Snake Game', width=250, height=250)
    self.border = curve(pos=[(-100,-100),(100,-100),(100,100),(-100,100)])
    self.scene.autoscale = False
    self.snake = box(pos=(0,0,0), length=4, width=4, height=4, color=color.red)

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
  
  def run(self):
    running = True

    try:
      time.sleep(.1)
      # Initialize connection to server
      self.conn.sendto("c", (self.addr, self.serverport))
      while running:
        #'Wait' function for discrete time?
        
        # select on specified file descriptors
        readable, writable, exceptional=(sel.select(self.read_list, self.write_list, []))
        for f in readable:
          if f is self.conn: #if a packet is received
            msg, addr = f.recvfrom(32)
            print(msg,addr)
            messages = []
            for inner_message in msg.split('|'):
              messages.append(inner_message)
            for position in messages[:-1]:
              coords = []
              for coord in position.split(','):
                coords.append(coord)
              x,y = int(float(coords[0])),int(float(coords[1]))
              print(type(x),y)
              self.snake.pos = vector(x,y,0)
              print(self.snake.pos)
              # except:
              #   pass  # If something goes wrong, don't draw anything.
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
    finally:
      self.conn.sendto("d", (self.addr, self.serverport))


if __name__ == "__main__":
  g = SnakeClient()
  g.run()