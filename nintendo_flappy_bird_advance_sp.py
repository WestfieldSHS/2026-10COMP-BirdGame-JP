# game may not contain any birds
# game may contain traces of cats
# flappy bird advance sp can also play gameboy and gameboy colour games
#  start modules
from cmath import pi
from random import randint
import pgzrun
import sys
import pip
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
gameoverscreen = Actor("gos")
# make bird
rand_cat = randint(1,4)
if rand_cat == 2:
    bird = Actor("ocat")
elif rand_cat == 3:
    bird = Actor("calcat")
elif rand_cat == 4:
    bird = Actor("ravencat")        
else:    
    bird = Actor("bird")
bird.x = 60
bird.y = 300
# make pipes
def random_centre():
    centre = randint(210,410)
    return centre
def random_gap():
    gap = randint(180,280)
    return gap

class pipes():
    def __init__(self, x, centre, gap):        
        self.top = Actor("top")
        self.top.y = centre - ((HEIGHT/2)+(gap/2))
        self.top.x = x
        self.bottom = Actor("bottom")
        self.bottom.y = centre + ((HEIGHT/2)+(gap/2))
        self.bottom.x = x

pipeList = []
pipe1 = pipes(266, 400, 220)
pipeList.append(pipe1)
pipe2 = pipes(532, 180, 220)
pipeList.append(pipe2)
pipe3 = pipes(798, 315, 220)
pipeList.append(pipe3)
# draw everything to screen
def draw():
     if gameOver == True:
        gameoverscreen.draw()
        screen.draw.text(f"Game Over!",topleft=(10,10),fontsize = 80,color ="darkblue")
        #score = 0
     if gameOver == False:
    # draw background
        background.draw()
    # draw characters
        bird.draw()
        for pipe in pipeList:
         pipe.top.draw()
         pipe.bottom.draw()
        screen.draw.text(f"Score: {score}",topleft=(10,10),fontsize=50)
# update everything
def update():
    global score
    global gameOver
    #print(score)
    # update bird
    bird.y = bird.y + 1.3
    # update pipes
    if gameOver == False:
        for pipe in pipeList:
            pipe.top.x = pipe.top.x - 5
            pipe.bottom.x = pipe.bottom.x - 5
            if pipe.top.x <= -44:
                score = score + 1
                print(f'Score: {score}')
                #pipe.top.x = 844
                #pipe.bottom.x = 844
                pipeList.remove(pipe)
                pipe = pipes(844,random_centre(),220)
                pipeList.append(pipe)
            if bird.colliderect(pipe.top):
                print("Hit!")
            # print(score)
                gameOver = True
                #sys.exit()
            if bird.colliderect(pipe.bottom):
                print("Hit!")
            # print(score)
                gameOver = True
                #sys.exit()    
            # bird hits bottom of screen
        if bird.y >HEIGHT:
            print("Game Over!")
            gameOver = True
            #sys.exit()
            # bird hits pipes

# moving
def on_mouse_down():
    bird.y = bird.y - 50
# runs everything
pgzrun.go()