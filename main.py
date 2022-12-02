#my final main file
'''
My final project is hunger man
a game




'''


'''
sources: 
https://www.youtube.com/@buildwithpython
https://www.w3schools.com/
https://www.101computing.net/pacman-ghost-algorithm/



'''
#importing libraries
import pygame as p
#built in libraries
#installed modules/library
#made libraries
from settings import *
from sprites import *


running=True



p.init()
screen=p.display.set_mode((WIDTH, HEIGHT))
time=p.time.Clock


while running==True:
    time.tick(FPS)

