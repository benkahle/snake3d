from visual import *
import random
import sys
import os
import time
import centerspot
from move_compass import move_compass

class Foodbox(object):
    def __init__(self):
        self.food=[]

#initial parameters
dt = 0.01
velocity=1

#creating game environment and welcome menu
tickcount=0
countbits=0
headlog=[]
snakeybits=[]
bit_objects = []
scene = display(title='Super-Mega Snake Game', width=750, height=750)
welcome = label(text='Welcome to Super-Mega Snake Game!\nX and Y axes are controlled with the arrow keys.\nZ axis is controlled by W and S.\nPress any direction to start.', align='center',pos=(0,0,0))
border = curve(pos=[(-100,-100,100),(100,-100,100),(100,-100,-100),(100,100,-100),(-100,100,-100),(-100,100,100),(-100,-100,100),(-100,-100,-100),(-100,100,-100),(-100,-100,-100),(100,-100,-100),(100,-100,100),(100,100,100),(100,100,-100),(100,100,100),(-100,100,100)])
scene.autoscale = False
snake = box(pos=(0,0,0), length=4, width=4, height=4, color=color.red)
welcomebox=box(pos=(0,0,100), length=1000, height=150, color=color.black)
snake.v = vector(0,0,0)
zboxs = curve(pos = [(-100,-100,snake.pos[2]),(100,-100,snake.pos[2]),(100,100,snake.pos[2]),(-100,100,snake.pos[2]),(-100,-100,snake.pos[2])], color = color.yellow)
yboxs = curve(pos = [(-100,snake.pos[1],-100),(100,snake.pos[1],-100),(100,snake.pos[1],100),(-100,snake.pos[1],100),(-100,snake.pos[1],-100)], color = color.yellow)
xboxs = curve(pos = [(snake.pos[0],-100,-100),(snake.pos[0],-100,100),(snake.pos[0],100,100),(snake.pos[0],100,-100),(snake.pos[0],-100,-100)], color = color.yellow)
#making compass
up = label(text='Up',align='center', pos=(0,10,-100), depth=0, color=color.green)
down = label(text='Down',align='center', pos=(0,-10,-100), depth=0, color=color.green)
s = label(text='s',align='center', pos=(0,-100,10), depth=0, color=color.green)
w = label(text='W',align='center', pos=(0,-100,-10), depth=0, color=color.green)
left = label(text='Left',align='center', pos=(snake.pos[0]-10,0,-100), depth=0, color=color.green)
right = label(text='Right',align='center', pos=(snake.pos[0]+10,0,-100), depth=0, color=color.green)

#creating food
foodbox=Foodbox()
food = box(pos=(random.randint(-96,96),random.randint(-96,96),random.randint(-96,96)), length=2, width=2, height=2, color=color.cyan)
foodbox.food.append(food)
foodsquare1 = curve(pos = [(-100,-100,food.pos[2]),(100,-100,food.pos[2]),(100,100,food.pos[2]),(-100,100,food.pos[2]),(-100,-100,food.pos[2])], color = color.green)
foodsquare2 = curve(pos = [(-100,food.pos[1],-100),(100,food.pos[1],-100),(100,food.pos[1],100),(-100,food.pos[1],100),(-100,food.pos[1],-100)], color = color.green)
foodsquare3 = curve(pos = [(food.pos[0],-100,-100),(food.pos[0],-100,100),(food.pos[0],100,100),(food.pos[0],100,-100),(food.pos[0],-100,-100)], color = color.green)
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def randpos(food):
    food.pos=(random.randint(-98,98),random.randint(-98,98),random.randint(-98,98))

def check_dir(snake):
    if scene.kb.keys: # is there an evcd UnicodeDecodeError()ent waiting to be processed?
        welcome.visible=0
        welcomebox.visible=0
        key = scene.kb.getkey() # obtain keyboard information
        if key == 'left' and snake.v!=vector(velocity,0,0):
            snake.v=vector(-velocity,0,0)
        if key == 'right' and snake.v!=vector(-velocity,0,0):
            snake.v=vector(velocity,0,0)
        if key == 'up' and snake.v!=vector(0, -velocity, 0):
            snake.v=vector(0,velocity,0)
        if key == 'down' and snake.v!=vector(0, velocity,0):
            snake.v=vector(0,-velocity,0)
        if key == 's' and snake.v!=vector(0,0, -velocity):
            snake.v=vector(0,0,velocity)
        if key == 'w' and snake.v!=vector(0,0, velocity):
            snake.v=vector(0,0,-velocity)
def check_wall(snake):
    if snake.pos[0]<= -98 or snake.pos[0]>= 98:
        return False
    elif snake.pos[1]<= -98 or snake.pos[1]>= 98:
        return False
    elif snake.pos[2]<= -98 or snake.pos[2]>= 98:
        return False
    else: return True
def check_snake(snake, countbits):
    n =2
    for i in bit_objects:
        if abs(snake.pos[0] - i.pos[0])<=n and abs(snake.pos[1] - i.pos[1])<=n and abs(snake.pos[2] - i.pos[2])<=n:
            return False
    return True
def zboxmove(snake):
    zboxs.pos = [(-100,-100,snake.pos[2]),(100,-100,snake.pos[2]),(100,100,snake.pos[2]),(-100,100,snake.pos[2]),(-100,-100,snake.pos[2])]
    yboxs.pos = [(-100,snake.pos[1],-100),(100,snake.pos[1],-100),(100,snake.pos[1],100),(-100,snake.pos[1],100),(-100,snake.pos[1],-100)]
    xboxs.pos = [(snake.pos[0],-100,-100),(snake.pos[0],-100,100),(snake.pos[0],100,100),(snake.pos[0],100,-100),(snake.pos[0],-100,-100)]
def checkfood():
    global countbits
    global velocity 
    global snakepos
    n=3
    for food in foodbox.food:
        if abs(snake.pos[0]-food.pos[0])<=n and abs(snake.pos[1]-food.pos[1])<=n and abs(snake.pos[2]-food.pos[2])<=n:
            randpos(food)
            foodsquare1.pos = [(-100,-100,food.pos[2]),(100,-100,food.pos[2]),(100,100,food.pos[2]),(-100,100,food.pos[2]),(-100,-100,food.pos[2])]
            foodsquare2.pos = [(-100,food.pos[1],-100),(100,food.pos[1],-100),(100,food.pos[1],100),(-100,food.pos[1],100),(-100,food.pos[1],-100)]
            foodsquare3.pos = [(food.pos[0],-100,-100),(food.pos[0],-100,100),(food.pos[0],100,100),(food.pos[0],100,-100),(food.pos[0],-100,-100)]
            countbits+=1
            snakeybits.append(str(countbits))
            item=box(pos=headlog[-400*int(countbits)], length=4, width=4, height=4, color=color.red)
            bit_objects.append(item)

def move_bits(bit_objects):
    for thing in bit_objects:
        thing.pos = headlog[-(bit_objects.index(thing)+1)*400]
def one_tick(snake):
    global tickcount
    global headlog
    global snakeybits
    checkfood()
    move_bits(bit_objects)
    check_dir(snake)
    zboxmove(snake)
    move_compass(snake,up,w,down,s,left,right)
    headlog.append(tuple(snake.pos))
    snake.pos += snake.v*dt
    tickcount+=1
    return tickcount and headlog
def end(): 
    scene.autoscale=True
    endtext = label(text='Game Over!', align='center',pos=[0,0,0], height = 30, color=color.red)
    options = label(text = 'Press P to play again', align = 'center', pos = [0,-50], color=color.yellow, height=10)
    x = True
    while x:
        key = scene.kb.getkey()
         # obtain keyboard information 
        if key == 'p':
            restart_program()          
def play():
    while check_wall(snake) and check_snake(snake, countbits):
        one_tick(snake)
        centerspot.centerspot(snake,scene,snake.v)
    end()

play()