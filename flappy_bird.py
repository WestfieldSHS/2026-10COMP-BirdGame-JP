# start modules
from cmath import pi

import pgzrun
import sys
# create constants
WIDTH = 800
HEIGHT = 600
score = 0
# print welcome
print('The game is about to start!')
print('Click the mouse to "flap" upwards')
print('Dodge the pipes and the floor')
print('Good luck and have fun!')
# make background
background = Actor("bg")
background.x = 400
background.y = 300
# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300
# make pipes
pipeList = []




topPipe1 = Actor("top")
topPipe1.x = 266
topPipe1.y = -10
pipeList.append(topPipe1)

bottomPipe1 = Actor("bottom")
bottomPipe1.x = 266
bottomPipe1.y = 800
pipeList.append(bottomPipe1)

topPipe2 = Actor("top")
topPipe2.x = 532
topPipe2.y = -200
pipeList.append(topPipe2)

bottomPipe2 = Actor("bottom")
bottomPipe2.x = 532
bottomPipe2.y = 560
pipeList.append(bottomPipe2)

topPipe3 = Actor("top")
topPipe3.x = 798
topPipe3.y = -120
pipeList.append(topPipe3)

bottomPipe3 = Actor("bottom")
bottomPipe3.x = 798
bottomPipe3.y = 710
pipeList.append(bottomPipe3)
# draw everything to screen
def draw():
    # draw background
    background.draw()
    # draw characters
    bird.draw()
    for pipe in pipeList:
        pipe.draw()
# update everything
def update():
    global score
    # update bird
    bird.y = bird.y + 1
    # update pipes
    for pipe in pipeList:
        pipe.x = pipe.x - 5
        if pipe.x <= -44:
            pipe.x = 800
        if pipe.image == "top":
            score = score + 1
        # bird hits bottom of screen
        if bird.y >HEIGHT:
            print('Game Over!')
            print(score)
            sys.exit()
        # bird hits pipes
    for pipe in pipeList:
        if bird.colliderect(pipe):
            print("Hit!")
            #sys.exit()
# moving
def on_mouse_down():
    bird.y = bird.y - 50
# runs everything
pgzrun.go()