from visual import *
import time
import Pyro4

class Snake(box):

    def check_dir(self):
        if scene.kb.keys:
            key = scene.kb.getkey()
            if key == 'left':
                self.v[0]=-1
                self.v[1]=0
            if key == 'right':
                self.v[0]=1
                self.v[1]=0
            if key == 'up':
                self.v[1]=1
                self.v[0]=0
            if key == 'down':
                self.v[1]=-1
                self.v[0]=0

    

def one_tick(snake,dt):
    if check_wall(snake):
        snake.pos += snake.v*dt
    else:
        pass
        #Quit the game/end

class Game(object):
    def __init__(self,dt):
        self.dt = dt
        self.world = curve(pos=[(-100,-100),(100,-100),(100,100),(-100,100),(-100,-100)])

    def check_wall(self,snake):
        if snake.pos[0]<= -100 or snake.pos[0]>= 100:
            return False
        else: return True

    def gameloop(self):
        if self.check_wall
def main():
    dt = 0.001
    p1 = Snake(pos=(6,0,0), length=4, width=4, height=4, color=color.red)
    p1.v = vector(0,0,0)
    scene.autoscale = False
    Pyro4.config.HOST=('192.168.134.147')
    daemon=Pyro4.Daemon()
    p1_uri = daemon.register(p1)
    ns=Pyro4.locateNS()
    ns.register('Snake3d.player1.snake',p1_uri)
    one_tick(p1,dt)
    daemon.requestLoop()

main()