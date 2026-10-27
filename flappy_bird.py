#  flappy_bird.py does not contain any actual birds
# flappy_bird.py may contain traces of cats
# flappy_bird_random.py is haunted
#  start modules
from cmath import pi
import pgzrun
import sys
# create constants
WIDTH = 800
HEIGHT = 600
score = 0
gameOver = False
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
bird.x = 80
bird.y = 300
# make pipes
pipeList = []



topPipe1 = Actor("top")
topPipe1.x = 366
topPipe1.y = -10
pipeList.append(topPipe1)

bottomPipe1 = Actor("bottom")
bottomPipe1.x = 366
bottomPipe1.y = 800
pipeList.append(bottomPipe1)


topPipe2 = Actor("top")
topPipe2.x = 732
topPipe2.y = -210
pipeList.append(topPipe2)

bottomPipe2 = Actor("bottom")
bottomPipe2.x = 732
bottomPipe2.y = 660
pipeList.append(bottomPipe2)

topPipe3 = Actor("top")
topPipe3.x = 998
topPipe3.y = -120
pipeList.append(topPipe3)

bottomPipe3 = Actor("bottom")
bottomPipe3.x = 998
bottomPipe3.y = 710
pipeList.append(bottomPipe3)
# draw everything to screen
def draw():
    if gameOver == True:
        screen.fill((0,0,0))
        screen.draw.text(f"Game Over!",topleft=(10,10),fontsize = 30)
        #score = 0
    if gameOver == False:
    # draw background
        background.draw()
    # draw characters
        bird.draw()
        for pipe in pipeList:
            pipe.draw()
        screen.draw.text(f"Score: {score}",topleft=(0,0),fontsize = 40)
# update everything
def update():
    global score
    global gameOver
    # update bird
    bird.y = bird.y + 1.3
    # update pipes
    for pipe in pipeList:
        pipe.x = pipe.x - 5
        if pipe.x <= -44:
            pipe.x = 800
        if pipe.image == "top":
            score = score + 1
        # bird hits bottom of screen
        if bird.y >HEIGHT:
            #print('Game Over!')
            #print(score)
            gameOver = True
        # bird hits pipes
        if bird.colliderect(pipe):
            print("Hit!")
            print("Game Over!")
            gameOver = True
# moving
def on_mouse_down():
    bird.y = bird.y - 60
# runs everything
pgzrun.go()