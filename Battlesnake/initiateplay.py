import os
from visual import *
from visual.controls import *


scene = display(width=750, height=750)
welcome = label(text='Welcome to Super-Mega Snake Game!',align='center',pos=(0,0,0), yoffset= 100, height = 25, color = color.magenta)
instructions = label(text='Please click one of the options below.',align='center',pos=(0,0,0),yoffset= 73, height = 10)

#blarg = curve(pos = [(-35,-63,0),(35,-34,0),(34,-44,0),(22,-15,0),(-100,-100,0)])

#DON'T CHANGE ANY OF THESE POSITIONS. Or any of the text. For real.
one = label(text = 'Single Player Mode', align='center',pos=(0,0,0), yoffset= 0,color = color.yellow)
two = label(text = 'Two Player Mode', align='center',pos=(0,0,0), yoffset= -55,color = color.yellow)
twodnet = label(text = 'Join a 2D Network Game', align='center',pos=(0,0,0), yoffset= -125, color = color.yellow)
threednet = label(text = 'Join a 3D Network Game', align='center',pos=(0,0,0), yoffset= -195, color = color.yellow)

while 1:
	if scene.mouse.clicked:
		m = scene.mouse.getclick()
		if m.pos[0]>=-2.85 and m.pos[0]<=2.85 and m.pos[1]>=-.51 and m.pos[1]<=.51:
			os.system('python vpythontests.py')
		elif m.pos[0]>=-2.5 and m.pos[0]<=2.5 and m.pos[1]>=-2.8 and m.pos[1]<=-1.75:
			os.system('python battlesnake.py')
		elif m.pos[0]>=-3.94 and m.pos[0]<=3.94 and m.pos[1]>=-5.04 and m.pos[1]<=-4.02:
			os.system('python base_snakeclient.py')
		elif m.pos[0]>=-3.94 and m.pos[0]<=3.94 and m.pos[1]>=-7.24 and m.pos[1]<=-6.18:		
			os.system('python 3d_snakeclient.py')
