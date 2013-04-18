from visual import *
import random
import sys
import os
import time
import centerspot

class Foodbox(object):
    def __init__(self):
        self.food=[]

#initial parameters
dt = 0.01
velocity=1

#creating game environment and welcome menu

scene = display(title='Super-Mega Snake Game', width=750, height=750)
welcome = label(text='Welcome to Super-Mega Snake Game!\n Player 1(purple) controlles X and Y axes are controlled with the arrow keys.\nZ axis is controlled by O and L.\n Player 2(yellow) is controlled by A, W, S, and D. \n Z axis is controlled by F and R. \n Press any direction to start.', align='center',pos=(0,0,0))
border = curve(pos=[(-100,-100,100),(100,-100,100),(100,-100,-100),(100,100,-100),(-100,100,-100),(-100,100,100),(-100,-100,100),(-100,-100,-100),(-100,100,-100),(-100,-100,-100),(100,-100,-100),(100,-100,100),(100,100,100),(100,100,-100),(100,100,100),(-100,100,100)])
scene.autoscale = False
snake = box(pos=(20,0,0), length=4, width=4, height=4, color=color.magenta)
snake2 = box(pos=(-10,0,0), length=4, width=4, height=4, color=color.yellow)
welcomebox=box(pos=(0,0,100), length=1000, height=150, color=color.black)
snake.v = vector(0,0,0)
snake2.v = vector(0,0,0)


#creating food
foodbox=Foodbox()
food = box(pos=(random.randint(-96,96),random.randint(-96,96),random.randint(-96,96)), length=2, width=2, height=2, color=color.cyan)
foodbox.food.append(food)
foodsquare = curve(pos = [(-100,-100,food.pos[2]),(100,-100,food.pos[2]),(100,100,food.pos[2]),(-100,100,food.pos[2]),(-100,-100,food.pos[2])], color = color.green)

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
        if key == 'l' and snake.v!=vector(0,0, -velocity):
            snake.v=vector(0,0,velocity)
        if key == 'o' and snake.v!=vector(0,0, velocity):
            snake.v=vector(0,0,-velocity)
def check_dir2(snake):
    if scene.kb.keys: # is there an evcd UnicodeDecodeError()ent waiting to be processed?
        welcome.visible=0
        welcomebox.visible=0
        key = scene.kb.getkey() # obtain keyboard information
        if key == 'a' and snake.v!=vector(velocity,0,0):
            snake.v=vector(-velocity,0,0)
        if key == 'd' and snake.v!=vector(-velocity,0,0):
            snake.v=vector(velocity,0,0)
        if key == 'w' and snake.v!=vector(0, -velocity, 0):
            snake.v=vector(0,velocity,0)
        if key == 's' and snake.v!=vector(0, velocity,0):
            snake.v=vector(0,-velocity,0)
        if key == 'f' and snake.v!=vector(0,0, -velocity):
            snake.v=vector(0,0,velocity)
        if key == 'r' and snake.v!=vector(0,0, velocity):
            snake.v=vector(0,0,-velocity)
def check_wall(snake):
    if snake.pos[0]<= -100 or snake.pos[0]>= 100:
        return False
    elif snake.pos[1]<= -100 or snake.pos[1]>= 100:
        return False
    elif snake.pos[2]<= -100 or snake.pos[2]>= 100:
        return False
    else: return True
def check_snake(snake, countbits, bit_objects):
    n =2
    for i in bit_objects:
        if abs(snake.pos[0] - i.pos[0])<=n and abs(snake.pos[1] - i.pos[1])<=n and abs(snake.pos[2] - i.pos[2])<=n:
            return False
    return True
def check_head(snake, snake2):
    n = 2 
   # print(abs (snake.pos[0] - snake2.pos[0]))# and abs(snake.pos[1] - snake2.pos[1]) and abs(snake.pos[2] - snake2.pos[2])
    if abs (snake.pos[0] - snake2.pos[0])<=n and abs(snake.pos[1] - snake2.pos[1])<=n and abs(snake.pos[2] - snake2.pos[2])<=n:
        return False
    return True

def zboxmove(snake, zbox):
    zbox.pos = [(-100,-100,snake.pos[2]),(100,-100,snake.pos[2]),(100,100,snake.pos[2]),(-100,100,snake.pos[2]),(-100,-100,snake.pos[2])]
def checkfood(snake, velocity, countbits, snakeybits, headlog, bit_objects,cala):
    # global countbits
    # global velocity 
    # global snakepos
    n=3
    for food in foodbox.food:
        if abs(snake.pos[0]-food.pos[0])<=n and abs(snake.pos[1]-food.pos[1])<=n and abs(snake.pos[2]-food.pos[2])<=n:
            randpos(food)
            foodsquare.pos = [(-100,-100,food.pos[2]),(100,-100,food.pos[2]),(100,100,food.pos[2]),(-100,100,food.pos[2]),(-100,-100,food.pos[2])]
            countbits+=1
            snakeybits.append(str(countbits))
            item=box(pos=headlog[-400*int(countbits)], length=4, width=4, height=4, color=snake.color)
            bit_objects.append(item)
    return countbits and snakeybits and bit_objects

def move_bits(bit_objects, headlog):
    for thing in bit_objects:
        thing.pos = headlog[-(bit_objects.index(thing)+1)*400]
def one_tick(snake, snakeybits, countbits, headlog, tickcount, bit_objects, zbox):
    # global tickcount
    # global headlog
    # global snakeybits
    checkfood(snake, velocity, countbits, snakeybits, headlog, bit_objects, 'magenta')
    move_bits(bit_objects, headlog)
    check_dir(snake)
    zboxmove(snake, zbox)
    headlog.append(tuple(snake.pos))
    snake.pos += snake.v*dt
    tickcount+=1
    return tickcount and headlog
def one_tick2(snake2, snakeybits2, countbits2, headlog2, tickcount2, bit_objects2, zbox2):
    # global tickcount
    # global headlog
    # global snakeybits
    checkfood(snake2, velocity, countbits2, snakeybits2, headlog2, bit_objects2, 'yellow')
    move_bits(bit_objects2, headlog2)
    check_dir2(snake2)
    zboxmove(snake2, zbox2)
    headlog2.append(tuple(snake2.pos))
    snake2.pos += snake2.v*dt
    tickcount2+=1
    return tickcount2 and headlog2

def end(win): 
    endtext = label(text='Game Over!', align='center',pos=[0,0,0], height = 30, color=color.red)
    winnertext = label(text=win, align='center',pos=[0,-30,0], height = 30, color=color.green)
    options = label(text = 'Press P to play again', align = 'center', pos = [0,-50], color=color.yellow, height=10)
    x = True
    while x:
        key = scene.kb.getkey()
         # obtain keyboard information 
        if key == 'p':
            restart_program()          
def play():
    tickcount=0
    tickcount2 = 0
    countbits=0
    countbits2 = 0
    headlog=[]
    headlog2 = []
    snakeybits=[]
    snakeybits2 = []
    bit_objects = []
    bit_objects2 = []
    zbox = curve(pos = [(-100,-100,snake.pos[2]),(100,-100,snake.pos[2]),(100,100,snake.pos[2]),(-100,100,snake.pos[2]),(-100,-100,snake.pos[2])], color = color.magenta)
    zbox2 = curve(pos = [(-100,-100,snake.pos[2]),(100,-100,snake.pos[2]),(100,100,snake.pos[2]),(-100,100,snake.pos[2]),(-100,-100,snake.pos[2])], color = color.yellow)

    while check_wall(snake) and check_snake(snake, countbits, bit_objects) and check_wall(snake2) and check_snake(snake2, countbits2, bit_objects2) and check_snake(snake, countbits2, bit_objects2) and check_snake(snake2, countbits, bit_objects) and check_head(snake, snake2):

        one_tick(snake, snakeybits, countbits, headlog, tickcount, bit_objects, zbox)
        one_tick2(snake2, snakeybits2, countbits2, headlog2, tickcount2, bit_objects2, zbox2)
        #centerspot.centerspot(snake,scene,snake.v)
    if not check_wall(snake) or not check_snake(snake, countbits, bit_objects) or not check_snake(snake, countbits2, bit_objects2):
        win = 'Player TWO Won!'
    if not check_wall(snake2) or not check_snake(snake2, countbits2, bit_objects2) or not check_snake(snake2, countbits, bit_objects):
        win = 'Player ONE Won!'
    if not check_head(snake, snake2):
        win = "It's a tie!"
    end(win)

play()


