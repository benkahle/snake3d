def move_compass(snake,up,w,down,s,left,right):
	up.pos = (0,snake.pos[1]+10,-100)
	down.pos = (0,snake.pos[1]-10,-100)
	w.pos = (0,-100,snake.pos[2]-10)
	s.pos = (0,-100,snake.pos[2]+10)
	left.pos = (snake.pos[0]-15,0,-100)
	right.pos = (snake.pos[0]+15,0,-100)
