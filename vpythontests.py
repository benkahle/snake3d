from visual import *
import random
import sys
import os
import time

class Foodbox(object):
    def __init__(self):
        self.food=[]
class Timestep(object):
    def __init__(self):
        self.timestep=[]

dt = Timestep()
dt.timestep=0.01
scene = display(title='Super-Mega Snake Game', width=750, height=750)
welcome = label(text='Welcome to Super-Mega Snake Game!\nX and Y axes are controlled with the arrow keys.\nZ axis is controlled by W and S.\nPress any direction to start.', align='center',pos=(0,0,0))
border = curve(pos=[(-100,-100,100),(100,-100,100),(100,-100,-100),(100,100,-100),(-100,100,-100),(-100,100,100),(-100,-100,100),(-100,-100,-100),(-100,100,-100),(-100,-100,-100),(100,-100,-100),(100,-100,100),(100,100,100),(100,100,-100),(100,100,100),(-100,100,100)])
scene.autoscale = False
snake = box(pos=(0,0,0), length=4, width=4, height=4, color=color.red)
welcomebox=box(pos=(0,0,100), length=1000, height=150, color=color.black)
snake.v = vector(0,0,0)
zbox = curve(pos = [(-100,-100,snake.pos[2]),(100,-100,snake.pos[2]),(100,100,snake.pos[2]),(-100,100,snake.pos[2]),(-100,-100,snake.pos[2])], color = color.yellow)

foodbox=Foodbox()
food = box(pos=(random.randint(-96,96),random.randint(-96,96),random.randint(-96,96)), length=2, width=2, height=2, color=color.cyan)
foodbox.food.append(food)
foodsquare = curve(pos = [(-100,-100,food.pos[2]),(100,-100,food.pos[2]),(100,100,food.pos[2]),(-100,100,food.pos[2]),(-100,-100,food.pos[2])], color = color.green)

#counter = 0
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def randpos(thingy):
    thingy.pos=(random.randint(-98,98),random.randint(-98,98),random.randint(-98,98))
def check_dir(snake):
    if scene.kb.keys: # is there an evcd UnicodeDecodeError()ent waiting to be processed?
        welcome.visible=0
        welcomebox.visible=0
        key = scene.kb.getkey() # obtain keyboard information
        if key == 'q':
            quit()
        if key == 'left':
            snake.v=vector(-1,0,0)
        if key == 'right':
            snake.v=vector(1,0,0)
        if key == 'up':
            snake.v=vector(0,1,0)
        if key == 'down':
            snake.v=vector(0,-1,0)
        if key == 's':
            snake.v=vector(0,0,1)
        if key == 'w':
            snake.v=vector(0,0,-1)
def check_wall(snake):
    if snake.pos[0]<= -100 or snake.pos[0]>= 100:
        return False
    elif snake.pos[1]<= -100 or snake.pos[1]>= 100:
        return False
    elif snake.pos[2]<= -100 or snake.pos[2]>= 100:
        return False
    else: return True
def zboxmove(snake):
    zbox.pos = [(-100,-100,snake.pos[2]),(100,-100,snake.pos[2]),(100,100,snake.pos[2]),(-100,100,snake.pos[2]),(-100,-100,snake.pos[2])]
def checkfood():
    n=3
    for food in foodbox.food:
        if abs(snake.pos[0]-food.pos[0])<=n and abs(snake.pos[1]-food.pos[1])<=n and abs(snake.pos[2]-food.pos[2])<=n:
            randpos(food)
            foodsquare.pos = [(-100,-100,food.pos[2]),(100,-100,food.pos[2]),(100,100,food.pos[2]),(-100,100,food.pos[2]),(-100,-100,food.pos[2])]
            dt.timestep+=.003
def one_tick(snake):
#    if check_wall(snake):
    checkfood()
    check_dir(snake)
    zboxmove(snake)
    snake.pos += snake.v*dt.timestep
def end(): 
    endtext = label(text='Game Over!', align='center',pos=[0,0,0], height = 30, color=color.red)
    options = label(text = 'Press P to play again', align = 'center', pos = [0,-50], color=color.yellow, height=10)
    x = True
    while x:
        key = scene.kb.getkey() # obtain keyboard information 
        if key == 'p':
            restart_program()   
        if key!=0:
            x=False        
def play():
    while check_wall(snake):
        one_tick(snake)
    end()

play()


