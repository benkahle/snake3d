import socket
import select as sel
import sys
import random
from visual import *
class SnakeServer(object):
	def __init__(self,port = 9007):
		self.listener = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.listener.bind(('10.41.64.143',9007))
		self.read_list = [self.listener] #receiving client packets here
		self.write_list = [] #List to send to clients
		self.players = {} #stored position and velocity by address
		# self.headlog = {}  #list of positions of past 
		# self.countbits = {} #number of bits which this snake has eaten
		# self.bit_objects = {}


	def do_movement(self,mv,player):
		vel=self.players[player]['velocity']
		if mv == ' ':
			vel == vel
		if mv == 'a':
			vel = (-2,0)
		if mv == 'b':
			vel = (2,0)
		if mv == 'c':
			vel = (0,2)
		if mv == 'd':
			vel = (0,-2)
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

	def check_death(self,player):
		pos = self.players[player]['pos']
		if pos[0]<= -100 or pos[0]>= 100:
			return False
		elif pos[1]<= -100 or pos[1]>= 100:
			return False
		# elif snake[2]<= -100 or snake[2]>= 100:
			#return False
		else:
			n =2
    		for person in self.players:
				for i in range(1,self.players[person]['countbits']):
					position=self.players[person]['headlog'][int(i)]
					if abs(self.players[person]['pos'][0] - position[0])<=n and abs(self.players[person]['pos'][1] - position[1])<=n:# and abs(snake.pos[2] - i.pos[2])<=n:
						return False
					else: 
						return True
	def checkfood(self, player, food):
		n=3
		if abs(self.players[player]['pos'][0]-food[0])<=n and abs(self.players[player]['pos'][1]-food[1])<=n: # and abs(snake.pos[2]-food.pos[2])<=n:
			food = (random.randint(-96,96),random.randint(-96,96))
			self.players[player]['countbits']+=1
           #@snakeybits.append(str(countbits))
            #item=box(pos=self.players[player][headlog][-200*int(self.players[player][countbits])], length=4, width=4, height=4, color=snake.color)
           # self.players[player][bit_objects].append(item)
		return food

	def run(self):
		print('waiting...')
		food = (random.randint(-96,96),random.randint(-96,96))
		try:
			while True:
				if len(self.players)>1:
					running_state = 'run'
					for player in self.players:
						self.change_pos(player)
						if self.check_death(player):
							running_state = player[1]

					send = []
					for player in self.players:
						self.players[player]['headlog'].append(self.players[player]['pos'])
						food = self.checkfood(player, food)
						self.players[player]['snakelog'] = self.players[player]['headlog'][-self.players[player]['countbits']:]
						print(self.players[player]['snakelog'])
						snake_pos_to_send = []
						for position in self.players[player]['snakelog']:
							snake_pos_to_send.append(str(position))
						send.append(';'.join(snake_pos_to_send))
					print(snake_pos_to_send)
					foodpos = str(food)
					send.append(foodpos)
					send.append(str(running_state))
					msg = '|'.join(send)
					print(msg)
					for player in self.players:
						print(player)
						self.listener.sendto(msg,player)

				readable,writable,exceptional = (sel.select(self.read_list,self.write_list,[],0.1))
				for f in readable:
					if f is self.listener:
						msg,addr = f.recvfrom(32)
						if len(msg) >= 1:
							cmd = msg[0]
							print(msg)
							if cmd == 'c': #New connection
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