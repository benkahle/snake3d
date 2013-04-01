from visual import *

dt = 0.001

border = curve(pos=[(-100,-100),(100,-100),(100,100),(-100,100),(-100,-100)])
snake = box(pos=(6,0,0), length=4, width=4, height=4, color=color.red)
snake.v = vector(0,0,0)
snake.origin = (0,0,0)
scene.autoscale = False
#counter = 0
def check_dir(snake):
    if scene.kb.keys: # is there an event waiting to be processed?
        key = scene.kb.getkey() # obtain keyboard information
        if key == 'left':
            snake.v[0]=-1
            snake.v[1]=0
        if key == 'right':
            snake.v[0]=1
            snake.v[1]=0
        if key == 'up':
            snake.v[1]=1
            snake.v[0]=0
        if key == 'down':
            snake.v[1]=-1
            snake.v[0]=0
def bounce(snake):
    print('bounce check:')
    if snake.pos[0]<= -100 or snake.pos[0]>= 100:
        print('x-error')
        snake.v[0] == -snake.v[0]
    if snake.pos[1]<= -100 or snake.pos[1]>= 100:
        print('y-error')
        snake.v[1] == -snake.v[1]
def one_tick(snake):
    check_dir(snake)
    bounce(snake)
    snake.pos += snake.v*dt

        

while 1:
    one_tick(snake)