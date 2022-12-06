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
player=Player()


p.init()
screen=p.display.set_mode((WIDTH, HEIGHT))
time=p.time.Clock

draw_text("Pick a difficulty, e for easy, m for medium, h for hard", 15, WHITE, WIDTH/2, HEIGHT/18)
for event in p.event.get():
    if event.type==p.KEYDOWN:
        if event.key==p.K_H:
            for i in range(100):
                m = Npc(5, 5, 25, 25, RED)
                allSprites.add(m)
                allnpcs.add(m)
                print(m)


while running==True:
    
    mobhits = p.sprite.spritecollide(player, allnpcs, True)
    if mobhits:
        print("ive struck a mob")
        SCORE += 1

    for event in p.event.get():
        # check for closed window
        if event.type == p.QUIT:
            running = False
       
        
    ############ Update ##############
    # update all sprites
    allSprites.update()

    ############ Draw ################
    # draw the background screen
    screen.fill(BLACK)
   
    # draw all sprites
    allSprites.draw(screen)

    # buffer - after drawing everything, flip display
    p.display.flip()

