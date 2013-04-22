from math import tan
def camera(snake,scene):
	R=40
	try:
		# camera=snake.pos-R*snake.v
		scene.forward=snake.pos
	except ValueError:
		pass
	scene.center=snake.pos-R*snake.v
	scene.range=R*tan(scene.fov/2)
	# scene.lights=[local_light(pos=snake.pos,color=color.yellow)]
	# scene.ambient=0


