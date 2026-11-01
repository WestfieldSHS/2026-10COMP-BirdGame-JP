# oh dear the python files are multiplying
#  start modules
from cmath import pi
import pgzrun
import sys
# create constants
WIDTH = 800
HEIGHT = 600
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
class pipes():
    def __init__(self, x, center, gap):
        Actor("top")
# draw everything to screen
def draw():
    # draw background
     background.draw()
    # draw characters
     bird.draw()            
# update everything
def update():
    # update bird
    bird.y = bird.y + 1.3
    # update pipes
    
        # bird hits bottom of screen
    if bird.y >HEIGHT:
        print("Game Over!")
        sys.exit()
        # bird hits pipes

# moving
def on_mouse_down():
    bird.y = bird.y - 50
# runs everything
pgzrun.go()