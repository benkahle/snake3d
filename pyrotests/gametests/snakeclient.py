import socket
import select
import random
import time

class SnakeClient(object):
  def __init__(self, addr="192.168.134.149", serverport=9009):
    self.clientport = random.randrange(8000, 8999)
    self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind to localhost - set to external ip to connect from other computers
    self.conn.bind(("192.168.134.149", self.clientport))
    self.addr = addr
    self.serverport = serverport
    self.read_list = [self.conn]
    self.write_list = []
    
    self.setup_game()
  
  def setup_pygame(self):
    #Setup vpython game world here

  def check_keyinput(self):
    if scene.kb.keys: # is there an evcd UnicodeDecodeError()ent waiting to be processed?
      welcome.visible=0
      welcomebox.visible=0
      key = scene.kb.getkey() # obtain keyboard information
      if key == 'left':
        cmd = 'a'
      if key == 'right':
        cmd = 'b'
      if key == 'up':
        cmd = 'c'
      if key == 'down':
        cmd = 'd'
      if key == 's':
        cmd = 'e'
      if key == 'w': 
        cmd = 'f'
    return cmd
  
  def run(self):
    running = True

    try:
      # Initialize connection to server
      self.conn.sendto("c", (self.addr, self.serverport))
      while running:
        #'Wait' function for discrete time
        
        # select on specified file descriptors
        readable, writable, exceptional=(select.select(self.read_list, self.write_list, [], 0))
        for f in readable:
          if f is self.conn: #if a packet is received
            msg, addr = f.recvfrom(32)
            for position in msg[:2].split('|'):
              x, sep, y, sep, z = position.partition(',')
              try:
                #Update position of each snake
              except:
                pass  # If something goes wrong, don't draw anything.
        self.conn.sendto("u"+self.check_keyinput, (self.addr, self.serverport))
    finally:
      self.conn.sendto("d", (self.addr, self.serverport))


if __name__ == "__main__":
  g = SnakeClient()
  g.run()