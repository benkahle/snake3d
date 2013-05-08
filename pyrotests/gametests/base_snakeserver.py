import socket
import select as sel
import sys
import random
import math
from visual import *
class SnakeServer(object):
	def __init__(self,port = 55555):
		self.listener = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.listener.bind(('10.41.24.109',55555))
		self.read_list = [self.listener] #receiving client packets here
		self.write_list = [] #List to send to clients
		self.players = {} #stored position and velocity by address

	def point_distance(self,p0,p1):
		return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

	def do_movement(self,mv,player):
		vel=self.players[player]['velocity']
		speed = int(math.ceil(.2*self.players[player]['countbits']+3))
		if mv == ' ':
			vel == vel
		if mv == 'a' and vel != (speed,0):
			vel = (-speed,0)
		if mv == 'b' and vel != (-speed,0):
			vel = (speed,0)
		if mv == 'c' and vel != (0,-speed):
			vel = (0,speed)
		if mv == 'd' and vel != (0,speed):
			vel = (0,-speed)
		if mv == 'e':
			#set V(z+)
			pass
		if mv == 'f':
			pass
			#set V(z-)
		self.players[player]['velocity']=vel

	def change_pos(self,player):
		pos=self.players[player]['pos']
		vel = self.players[player]['velocity']
		pos = (pos[0] + vel[0],pos[1]+vel[1])
		self.players[player]['pos']=pos

	def is_dead(self,player):
		pos = self.players[player]['pos']
		if pos[0]<= -100 or pos[0]>= 100:
			return True
		elif pos[1]<= -100 or pos[1]>= 100:
			return True
		# elif snake[2]<= -100 or snake[2]>= 100:
			#return False
		else:
			n=2
			for meta_person in self.players:
				for position in self.players[meta_person]['snakepos'][1:]:
					if self.point_distance(self.players[player]['pos'],position) < 2:
						return True
			return False
	def checkfood(self, player, food):
		n=3
		if abs(self.players[player]['pos'][0]-food[0])<=n and abs(self.players[player]['pos'][1]-food[1])<=n: # and abs(snake.pos[2]-food.pos[2])<=n:
			food = (random.randint(-96,96),random.randint(-96,96))
			self.players[player]['countbits']+=1
		return food

	def run(self):
		print('waiting...')
		food = (random.randint(-96,96),random.randint(-96,96))
		try:
			while True:
				if len(self.players)>1:
					running_state = True
					for player in self.players:
						self.change_pos(player)
						if self.is_dead(player):
							running_state = False

					send = []
					for player in self.players:
						self.players[player]['headlog'].append(self.players[player]['pos'])
						food = self.checkfood(player, food)
						self.players[player]['snakepos'] = self.players[player]['headlog'][-self.players[player]['countbits']:]
						snake_pos_to_send = []
						for position in self.players[player]['snakepos']:
							snake_pos_to_send.append(str(position))
						send.append(';'.join(snake_pos_to_send))
					foodpos = str(food)
					send.append(foodpos)
					send.append(str(running_state))
					msg = '|'.join(send)
					#print(msg)
					for player in self.players:
						self.listener.sendto(msg,player)

				readable,writable,exceptional = (sel.select(self.read_list,self.write_list,[],0.075))
				for f in readable:
					if f is self.listener:
						msg,addr = f.recvfrom(32)
						if len(msg) >= 1:
							cmd = msg[0]
							if cmd == 'c': #New connection
								print('New Connection Established...')
								self.players[addr] = {'pos':(random.randint(-50,50),random.randint(-50,50)), 'velocity':(0,0), 'headlog':[], 'countbits':1, 'snakepos':[]} 
							elif cmd == 'u': #Movement update
								if len(msg) >= 2 and addr in self.players:
									self.do_movement(msg[1],addr)
							elif cmd == 'd':
								if addr in self.players:
									del self.players[addr]
							else:
								print("unexpected: {0}".format(msg))
		except KeyboardInterrupt as e:
			pass

if __name__ == '__main__':
	g = SnakeServer()
	g.run()