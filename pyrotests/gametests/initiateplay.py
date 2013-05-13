import os
import subprocess
from visual import *
from visual.controls import *


scene = display(width=750, height=750)
welcome = label(text='Welcome to Super-Mega Snake Game!',align='center',pos=(0,0,0), yoffset= 100, height = 25, color = color.magenta)
instructions = label(text='Please click one of the options below.',align='center',pos=(0,0,0),yoffset= 73, height = 10)
scene.autoscale = 0

#DON'T CHANGE ANY OF THESE POSITIONS. Or any of the text. For real.
one = label(text = 'Single Player Mode', align='center',pos=(0,0,0), yoffset= 0,color = color.yellow)
two = label(text = 'Two Player Mode', align='center',pos=(0,0,0), yoffset= -55,color = color.yellow)
twodnet = label(text = 'Join a 2D Network Game', align='center', xoffset=-135, pos=(-.5,0,0),yoffset= -135, color = color.yellow)
threednet = label(text = 'Join a 3D Network Game', align='center',xoffset=-150,pos=(0,0,0), yoffset= -205, color = color.yellow)
twohost = label(text = 'Host a 2D Network Game', align='center', xoffset=135, pos=(.5,0,0),yoffset= -135, color = color.yellow)
threehost = label(text = 'Host a 3D Network Game', align='center', xoffset=150, pos=(0,0,0),  yoffset= -205, color = color.yellow)




while 1:
	if scene.mouse.clicked:
		m = scene.mouse.getclick()

		#locals
		if m.pos[0]>=-2.85 and m.pos[0]<=2.85 and m.pos[1]>=-.51 and m.pos[1]<=.51:
			os.system('python vpythontests.py')
		elif m.pos[0]>=-2.5 and m.pos[0]<=2.5 and m.pos[1]>=-2.8 and m.pos[1]<=-1.75:
			os.system('python battlesnake.py')
		
		#joins
		elif m.pos[0]>=-8.43 and m.pos[0]<=-1.227 and m.pos[1]>=-5.355 and m.pos[1]<=-4.3:
			os.system('python base_snakeclient.py')
		elif m.pos[0]>=-8.43 and m.pos[0]<=-1.227 and m.pos[1]>=-7.62 and m.pos[1]<=-6.567:		
			os.system('python 3d_snakeclient.py')
		
		#hosts
		elif m.pos[0]>=1.1 and m.pos[0]<=8.53 and m.pos[1]>=-5.355 and m.pos[1]<=-4.3:
			os.system('python base_snakeserver.py')
			os.system('python base_snakeclient.py')
		elif m.pos[0]>=1.1 and m.pos[0]<=8.53 and m.pos[1]>=-7.62 and m.pos[1]<=-6.567:		
			os.system('python 3d_snakeserver.py')
			os.system('python 3d_snakeclient.py')
