import socket
import select as sel
import random
import time
import re
from visual import *

class SnakeClient(object):
	def __init__(self, addr="192.168.172.144", serverport=55557):
		self.clientport = random.randint(8000, 8999)
		self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.addr = addr
		self.serverport = serverport
		self.read_list = [self.conn]
		self.write_list = []
		self.setup_game()
  
	def setup_game(self):
		#Setup vpython game world here
		self.scene = display(title='Super-Mega Snake Game: Networked 3D', width=750, height=775)
		border = curve(pos=[(-100,-100,100),(100,-100,100),(100,-100,-100),(100,100,-100),(-100,100,-100),(-100,100,100),(-100,-100,100),(-100,-100,-100),(-100,100,-100),(-100,-100,-100),(100,-100,-100),(100,-100,100),(100,100,100),(100,100,-100),(100,100,100),(-100,100,100)])
		self.scene.autoscale = False
		self.p1_boxes = []
		self.p2_boxes = []
		self.zbox1 = curve(pos=[(-100,-100,0),(100,-100,0),(100,100,0),(-100,100,0),(-100,-100,0)],color=color.magenta)
		self.ybox1 = curve(pos=[(100,0,100),(100,0,-100),(-100,0,-100),(-100,0,100),(100,0,100)], color=color.magenta)
		self.zbox2 = curve(pos=[(-100,-100,0),(100,-100,0),(100,100,0),(-100,100,0),(-100,-100,0)],color=color.yellow)
		self.ybox2 = curve(pos=[(100,0,100),(100,0,-100),(-100,0,-100),(-100,0,100),(100,0,100)], color=color.yellow)
		self.zbox3 = curve(pos=[(-100,-100,0),(100,-100,0),(100,100,0),(-100,100,0),(-100,-100,0)],color=color.cyan)
		self.ybox3 = curve(pos=[(100,0,100),(100,0,-100),(-100,0,-100),(-100,0,100),(100,0,100)], color=color.cyan)
		# self.idx = box(pos=(20,0,0),length=3,width=3,height=3, color=color.red)
		# self.idy = box(pos=(0,20,0),length=3,width=3,height=3, color=color.green)
		# self.idz = box(pos=(0,0,100),length=3,width=3,height=3, color=color.blue)
		self.food_box = sphere(pos=(100,100,100),length=3,width=3,height=3,color=color.cyan)

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

	def zboxmove(self,coords, zbox, ybox):
		zbox.pos = [(-100,-100,coords[-1][2]),(100,-100,coords[-1][2]),(100,100,coords[-1][2]),(-100,100,coords[-1][2]),(-100,-100,coords[-1][2])]
		ybox.pos = [(-100,coords[-1][1],-100),(100,coords[-1][1],-100),(100,coords[-1][1],100),(-100,coords[-1][1],100),(-100,coords[-1][1],-100)]

	def foodzboxmove(self,coords):
		self.zbox3.pos = [(-100,-100,coords[2]),(100,-100,coords[2]),(100,100,coords[2]),(-100,100,coords[2]),(-100,-100,coords[2])]
		self.ybox3.pos = [(-100,coords[1],-100),(100,coords[1],-100),(100,coords[1],100),(-100,coords[1],100),(-100,coords[1],-100)]

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
					msg, sentaddr = f.recvfrom(16384)
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
						p1_coords.append(vector(int(positions[0]),int(positions[1]),int(positions[2])))
					for position in messages[1].split(';'): #snake '2'
						position = re.sub('[\(\)]','',position)
						positions = []
						for i in position.split(','):
							positions.append(i)
						p2_coords.append(vector(int(positions[0]),int(positions[1]),int(positions[2])))
					self.make_snake(p1_coords,'p1')
					self.zboxmove(p1_coords,self.zbox1,self.ybox1)
					self.make_snake(p2_coords,'p2')
					self.zboxmove(p2_coords,self.zbox2,self.ybox2)
					position = messages[2] #food
					position = re.sub('[\(\)]','',position)
					positions = []
					for i in position.split(','):
						positions.append(i)
					food_loc = vector(int(positions[0]),int(positions[1]),int(positions[2]))
					self.food_box.pos = food_loc
					self.foodzboxmove(food_loc)
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
						loss_text = label(text='Game Over!', align='center',pos=(0,0,0),height=30,color=color.red)
						running = False

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
				if key == 'w':
					self.conn.sendto('ue',(self.addr, self.serverport))
				if key == 's':
					self.conn.sendto('uf',(self.addr, self.serverport))
				if key == 'q':
					running = False
					self.conn.sendto("d", (self.addr, self.serverport))

if __name__ == "__main__":
	g = SnakeClient()
	g.run()