import socket
import select as sel
import random
import time
from visual import *

class SnakeClient(object):
  def __init__(self, addr="192.168.134.151", serverport=9008):
    self.clientport = random.randint(8000, 8999)
    self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind to localhost - set to external ip to connect from other computers
    self.conn.bind(("192.168.134.151", self.clientport))
    self.addr = addr
    self.serverport = serverport
    self.read_list = [self.conn]
    self.write_list = []
    
    self.setup_game()
  
  def setup_game(self):
    #Setup vpython game world here
    scene = display(title='Super-Mega Snake Game', width=250, height=250)
    border = curve(pos=[(-100,-100),(100,-100),(100,100),(-100,100)])
    scene.autoscale = False
    snake = box(pos=(0,0), length=4, width=4, height=4, color=color.red)

  def check_keyinput(self):
    cmd = ' '
    if scene.kb.keys: # is there an evcd UnicodeDecodeError()ent waiting to be processed?
      # welcome.visible=0
      # welcomebox.visible=0
      key = scene.kb.getkey() # obtain keyboard information
      if key == 'left':
        cmd = 'a'
      if key == 'right':
        cmd = 'b'
      if key == 'up':
        cmd = 'c'
      if key == 'down':
        cmd = 'd'
      # if key == 's':
      #   cmd = 'e'
      # if key == 'w': 
      #   cmd = 'f'
    return cmd
  
  def run(self):
    running = True

    try:
      time.sleep(1)
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
            for position in msg[:2].split('|'):
              x, sep, y = position.partition(',')
              try:
                snake.pos =(x,y)
              except:
                pass  # If something goes wrong, don't draw anything.
        print('u'+str(self.check_keyinput()))
        self.conn.sendto("u"+str(self.check_keyinput()), (self.addr, self.serverport))
    finally:
      self.conn.sendto("d", (self.addr, self.serverport))


if __name__ == "__main__":
  g = SnakeClient()
  g.run()