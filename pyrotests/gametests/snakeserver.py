import socket
import select as sel
import sys
from visual import *
class SnakeServer(object):
	def __init__(self,port = 9007):
		self.listener = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.listener.bind(('10.41.24.86',9007))
		self.read_list = [self.listener] #receiving client packets here
		self.write_list = [] #List to send to clients
		self.players = {} #stored position and velocity by address
		# self.headlog = {}  #list of positions of past 
		# self.countbits = {} #number of bits which this snake has eaten
		# self.bit_objects = {}


	def do_movement(self,mv,player):
		vel=self.players[player][1]
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
		self.players[player][1]=vel
		self.change_pos(player)

	def change_pos(self,player):
		pos=self.players[player]['pos']
		vel = self.players[player]['velocity']
		pos = pos + vel
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
				for i in range(1,self.players[player]['countbits']+1):
					position=headlog[-200*int(i)]
					if abs(self.players[player]['pos'][0] - position[0])<=n and abs(self.players[player]['pos'][1] - position[1])<=n:# and abs(snake.pos[2] - i.pos[2])<=n:
						return False
					else: 
						return True
	def checkfood(self, player, food):
		n=3
		if abs(self.players[player]['pos'][0]-food[0])<=n and abs(self.players[player]['pos'][1]-food[1])<=n: # and abs(snake.pos[2]-food.pos[2])<=n:
			food = [random.randint(-96,96),random.randint(-96,96)]
			self.players[player]['countbits']+=1
           #@snakeybits.append(str(countbits))
            #item=box(pos=self.players[player][headlog][-200*int(self.players[player][countbits])], length=4, width=4, height=4, color=snake.color)
           # self.players[player][bit_objects].append(item)
		return self

	def run(self):
		print('waiting...')
		food = (random.randint(-96,96),random.randint(-96,96))
		# foodbox.food.append(food)
		# foodsquare1 = curve(pos = [(-100,-100,food.pos[2]),(100,-100,food.pos[2]),(100,100,food.pos[2]),(-100,100,food.pos[2]),(-100,-100,food.pos[2])], color = color.green)
		# foodsquare2 = curve(pos = [(-100,food.pos[1],-100),(100,food.pos[1],-100),(100,food.pos[1],100),(-100,food.pos[1],100),(-100,food.pos[1],-100)], color = color.green)
		try:
			while True:
				readable,writable,exceptional = (sel.select(self.read_list,self.write_list,[]))
				for f in readable:
					if f is self.listener:
						msg,addr = f.recvfrom(32)
						if len(msg) >= 1:
							cmd = msg[0]
							print(msg)
							if cmd == 'c': #New connection
								self.players[addr] = {'pos':(0,0), 'velocity':(0,0), 'headlog':[], 'countbits':0, 'snakepos':[]} 
							elif cmd == 'u': #Movement update
								if len(msg) >= 2 and addr in self.players:
									self.do_movement(msg[1],addr)
							elif cmd == 'd':
								if addr in self.players:
									del self.players[addr]
							else:
								print("unexpected: {0}".format(msg))
				running_state = True
				for player in self.players:
					if self.check_death(player):
						running_state = False
				for player in self.players:
					self.players[player]['headlog'].append(self.players[player]['pos'])
					self.checkfood(player, food)
					self.players[player]['snakelog'] = self.players[player]['headlog'][-self.players[player]['countbits']:400:]
					snake_pos_to_send = []
					for position in self.players[player]['snakelog']:
						snake_pos_to_send.append(str(position))

					send = []
					send.append(','.join(snake_pos_to_send))
					foodpos = str(food)
					send.append(foodpos)
					send.append(str(running_state))
					msg = '|'.join(send)
					print(msg)
					self.listener.sendto(msg,player)
					print(send)
		except KeyboardInterrupt as e:
			pass

if __name__ == '__main__':
	g = SnakeServer()
	g.run()