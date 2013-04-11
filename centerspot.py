def centerspot(snake):
    if snake.v[0]==0 and snake.v[1] == 0:
        if snake.v[2] > 0:
            scene.center = (snake.pos[0],snake.pos[1],snake.pos[2] + 1)
        elif snake.v[2] < 0:
            scene.center = (snake.pos[0],snake.pos[1],snake.pos[2]-1)
        else:
            scene.center = (snake.pos[0],snake.pos[1],snake.pos[2])
    elif snake.v[0]==0 and snake.v[2]==0:
        if snake.v[1] > 0:
            scene.center = (snake.pos[0],snake.pos[1]+1,snake.pos[2])
        elif snake.v[1] < 0:
            scene.center = (snake.pos[0],snake.pos[1]-1, snake.pos[2])
        else:
            scene.center = (snake.pos[0],snake.pos[1],snake.pos[2])
    elif snake.v[1]==0 and snake.v[2]==0:
        if snake.v[0] > 0:
            scene.center = (snake.pos[0]+1,snake.pos[1],snake.pos[2])
        elif snake.v[0] < 0:
            scene.center = (snake.pos[0]-1,snake.pos[1],snake.pos[2])
        else:
            scene.center = (snake.pos[0],snake.pos[1], snake.pos[2])
    centerspot=scene.center
    return centerspot