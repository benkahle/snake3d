from visual import *

dt = 0.001

border = curve(pos=[(-100,-100,100),(100,-100,100),(100,-100,-100),(100,100,-100),(-100,100,-100),(-100,100,100),(-100,-100,100),(-100,-100,-100),(-100,100,-100),(-100,-100,-100),(100,-100,-100),(100,-100,100),(100,100,100),(100,100,-100),(100,100,100),(-100,100,100)])
#grid1 = curve(pos=[(-100,-100,z)])
snake = box(pos=(6,0,0), length=4, width=4, height=4, color=color.red)
snake.v = vector(0,0,0)
snake.origin = (0,0,0)
scene.autoscale = False
#counter = 0
def check_dir(snake):
    if scene.kb.keys: # is there an evcd UnicodeDecodeError()ent waiting to be processed?
        key = scene.kb.getkey() # obtain keyboard information
        if key == 'left':
            snake.v=vector(-1,0,0)
        if key == 'right':
            snake.v=vector(1,0,0)
        if key == 'up':
            snake.v=vector(0,1,0)
        if key == 'down':
            snake.v=vector(0,-1,0)
        if key == 'w':
            snake.v=vector(0,0,1)
        if key == 's':
            snake.v=vector(0,0,-1)
def check_wall(snake):
    if snake.pos[0]<= -100 or snake.pos[0]>= 100:
        return False
    elif snake.pos[1]<= -100 or snake.pos[1]>= 100:
        return False
    else: return True
def one_tick(snake):
    if check_wall(snake):
        check_dir(snake)
        snake.pos += snake.v*dt
    else:
        pass
        #endtext = text(text='Game Over!', align='center',pos=[0,0,0], color=color.red)
        #This should work, but isn't for some reason

while 1:
    one_tick(snake)

# HI GUYS!