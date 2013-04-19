import socket
import select
import sys

class SnakeServer(object):
    def __init__(self,port = 9009):
        self.listener = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.listener.bind(('192.168.134.149',9009))
        self.read_list = [self.listener] #receiving client packets here
        self.write_list = [] #List to send to clients
        self.players = {} #stored position and velocity by address

    def do_movement(self,mv,player):
        vel=self.players[player][1]
        if mv = 'a':
            #set V(x+)
        if mv = 'b':
            #set V(x-)
        if mv = 'c':
            #set V(y+)
        if mv = 'd':
            #set V(y-)
        if mv = 'e':
            #set V(z+)
        if mv = 'f':
            #set V(z-)
        self.players[player][1]=vel
        self.change_pos(player)

    def change_pos(self,player):
        pos=self.players[player][0]
        #update player position with current velocity
        self.players[player][0]=pos

    def check_death(self,played):
        pos = self.players[player][0]
        #Check for collisions
        #if collision:
        #    return True    
        #else:
        #    return False
    
    def run(self):
        print('waiting...')
        try:
            while True:
                readable,writable,exceptional = (select.select(self.read_list,self.write_list,[]))
                for f in readable:
                    if f is self.listener:
                        msg,addr = f.recvfrom(32)
                        if len(msg) >= 1:
                            cmd = msg[0]
                            if cmd == 'c': #New connection
                                self.players[addr] = ((0,0,0),(0,0,0)) #((pos),(vel))
                            elif cmd == 'u': #Movement update
                                if len(msg) >= 2 and addr in self.players:
                                    self.do_movement(msg[1],addr)
                            elif cmd == 'd':
                                if addr in self.players:
                                    del self.players[addr]
                            else:
                                print("unexpected: {0}".format(msg))
                for player in self.players:
                    running_state = self.check_death(player)
                    send = []
                    for pos in self.players:
                        send.append("{0}{1}{2}".format(*self.players[pos][0]))
                    self.append(runningstate)
                    self.listener.sendto('|'.join(send),player)
        except KeyboardInterrupt as e:
            pass
            
if __name__ == '__main__':
    g = SnakeServer()
    g.run()