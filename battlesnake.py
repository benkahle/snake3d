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
dt = 0.020
velocity=1

#creating game environment and welcome menu
scene = display(title='Super-Mega Snake Game', width=750, height=750)
welcome = label(text='Welcome to Super-Mega Snake Game!',align='center',pos=(0,0,0), yoffset= 60, height = 25)
welcome_purple = label(text = 'Player 1(purple): \nArrow keys control X & Y axes.\nO and L control Z axis', align='center',pos=(0,0,0), color = color.magenta, xoffset= -20)
welcome_yellow = label(text = 'Player 2(yellow): \nA, W, S, and D control X & Y axes. \nF and R control Z axis', align='center',pos=(0,0,0), color = color.yellow, xoffset = 20 )
welcome_go = label(text = 'Press any direction to start.', align='center',pos=(0,0,0), yoffset=-60 )
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
foodsquare1 = curve(pos = [(-100,-100,food.pos[2]),(100,-100,food.pos[2]),(100,100,food.pos[2]),(-100,100,food.pos[2]),(-100,-100,food.pos[2])], color = color.green)
foodsquare2 = curve(pos = [(-100,food.pos[1],-100),(100,food.pos[1],-100),(100,food.pos[1],100),(-100,food.pos[1],100),(-100,food.pos[1],-100)], color = color.green)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def randpos(food):
    food.pos=(random.randint(-98,98),random.randint(-98,98),random.randint(-98,98))

def check_dir(snake, snake2):
    if scene.kb.keys: # is there an evcd UnicodeDecodeError()ent waiting to be processed?
        welcome.visible=0
        welcomebox.visible=0
        welcome_yellow.visible=0
        welcome_purple.visible=0
        welcome_go.visible=0
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
# def check_dir2(snake):
#     if scene.kb.keys: # is there an evcd UnicodeDecodeError()ent waiting to be processed?
#         welcome.visible=0
#         welcomebox.visible=0
#         key = scene.kb.getkey() # obtain keyboard information
        if key == 'a' and snake2.v!=vector(velocity,0,0):
            snake2.v=vector(-velocity,0,0)
        if key == 'd' and snake2.v!=vector(-velocity,0,0):
            snake2.v=vector(velocity,0,0)
        if key == 'w' and snake2.v!=vector(0, -velocity, 0):
            snake2.v=vector(0,velocity,0)
        if key == 's' and snake2.v!=vector(0, velocity,0):
            snake2.v=vector(0,-velocity,0)
        if key == 'f' and snake2.v!=vector(0,0, -velocity):
            snake2.v=vector(0,0,velocity)
        if key == 'r' and snake2.v!=vector(0,0, velocity):
            snake2.v=vector(0,0,-velocity)
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
    if abs (snake.pos[0] - snake2.pos[0])<=n and abs(snake.pos[1] - snake2.pos[1])<=n and abs(snake.pos[2] - snake2.pos[2])<=n:
        return False
    return True

def zboxmove(snake, zbox, ybox):
    zbox.pos = [(-100,-100,snake.pos[2]),(100,-100,snake.pos[2]),(100,100,snake.pos[2]),(-100,100,snake.pos[2]),(-100,-100,snake.pos[2])]
    ybox.pos = [(-100,snake.pos[1],-100),(100,snake.pos[1],-100),(100,snake.pos[1],100),(-100,snake.pos[1],100),(-100,snake.pos[1],-100)]
def checkfood(snake, velocity, countbits, snakeybits, headlog, bit_objects,cala):
    n=3
    for food in foodbox.food:
        if abs(snake.pos[0]-food.pos[0])<=n and abs(snake.pos[1]-food.pos[1])<=n and abs(snake.pos[2]-food.pos[2])<=n:
            randpos(food)
            foodsquare1.pos = [(-100,-100,food.pos[2]),(100,-100,food.pos[2]),(100,100,food.pos[2]),(-100,100,food.pos[2]),(-100,-100,food.pos[2])]
            foodsquare2.pos = [(-100,food.pos[1],-100),(100,food.pos[1],-100),(100,food.pos[1],100),(-100,food.pos[1],100),(-100,food.pos[1],-100)]
            countbits+=1
            snakeybits.append(str(countbits))
            item=box(pos=headlog[-200*int(countbits)], length=4, width=4, height=4, color=snake.color)
            bit_objects.append(item)
    return countbits and snakeybits and bit_objects

def move_bits(bit_objects, headlog):
    for thing in bit_objects:
        thing.pos = headlog[-(bit_objects.index(thing)+1)*200]
def one_tick(snake, snake2, snakeybits, countbits, headlog, tickcount, bit_objects, zbox, ybox):
    checkfood(snake, velocity, countbits, snakeybits, headlog, bit_objects, 'magenta')
    move_bits(bit_objects, headlog)
    check_dir(snake, snake2)
    zboxmove(snake, zbox, ybox)
    headlog.append(tuple(snake.pos))
    snake.pos += snake.v*dt
    tickcount+=1
    return tickcount and headlog
def one_tick2(snake2, snake, snakeybits2, countbits2, headlog2, tickcount2, bit_objects2, zbox2, ybox2):
    checkfood(snake2, velocity, countbits2, snakeybits2, headlog2, bit_objects2, 'yellow')
    move_bits(bit_objects2, headlog2)
    check_dir(snake, snake2)
    zboxmove(snake2, zbox2, ybox2)
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
    # zbox = curve(pos = [(-100,-100,snake.pos[2]),(100,-100,snake.pos[2]),(100,100,snake.pos[2]),(-100,100,snake.pos[2]),(-100,-100,snake.pos[2])], color = color.magenta)
    # zbox2 = curve(pos = [(-100,-100,snake.pos[2]),(100,-100,snake.pos[2]),(100,100,snake.pos[2]),(-100,100,snake.pos[2]),(-100,-100,snake.pos[2])], color = color.yellow)
    zbox = curve(pos = [(-100,-100,snake.pos[2]),(100,-100,snake.pos[2]),(100,100,snake.pos[2]),(-100,100,snake.pos[2]),(-100,-100,snake.pos[2])], color = color.magenta)
    ybox = curve(pos = [(-100,snake.pos[1],-100),(100,snake.pos[1],-100),(100,snake.pos[1],100),(-100,snake.pos[1],100),(-100,snake.pos[1],-100)], color = color.magenta)   
    zbox2 = curve(pos = [(-100,-100,snake2.pos[2]),(100,-100,snake2.pos[2]),(100,100,snake2.pos[2]),(-100,100,snake2.pos[2]),(-100,-100,snake2.pos[2])], color = color.yellow)
    ybox2 = curve(pos = [(-100,snake2.pos[1],-100),(100,snake2.pos[1],-100),(100,snake2.pos[1],100),(-100,snake2.pos[1],100),(-100,snake2.pos[1],-100)], color = color.yellow)   

    while check_wall(snake) and check_snake(snake, countbits, bit_objects) and check_wall(snake2) and check_snake(snake2, countbits2, bit_objects2) and check_snake(snake, countbits2, bit_objects2) and check_snake(snake2, countbits, bit_objects) and check_head(snake, snake2):
        # if scene.kb.keys: # is there an evcd UnicodeDecodeError()ent waiting to be processed?
        # welcome.visible=0
        # welcomebox.visible=0
        # key = scene.kb.getkey() #     
        # if key == 'd' or key == 'a' or key == 'w' or key == 'f' or  key == 'r' or  key == 'l' or key == 'o' or key == 'up' or key == 'down' or key == 'left' or key == 'right':
        #     check_dir(snake)
        #     print('hi')
        #     check_dir2(snake2)
        # else:
        one_tick(snake, snake2, snakeybits, countbits, headlog, tickcount, bit_objects, zbox, ybox)
        one_tick2(snake2, snake, snakeybits2, countbits2, headlog2, tickcount2, bit_objects2, zbox2, ybox2)
        #centerspot.centerspot(snake,scene,snake.v)
    if not check_wall(snake) or not check_snake(snake, countbits, bit_objects) or not check_snake(snake, countbits2, bit_objects2):
        win = 'Player 2 Won!'
    if not check_wall(snake2) or not check_snake(snake2, countbits2, bit_objects2) or not check_snake(snake2, countbits, bit_objects):
        win = 'Player 1 Won!'
    if not check_head(snake, snake2):
        win = "It's a tie!"
    end(win)

play()


