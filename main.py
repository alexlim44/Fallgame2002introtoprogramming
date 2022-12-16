#my final main file
'''
My final project is hunger man
a game



ALEX LIM
'''


'''
sources: 
https://www.youtube.com/@buildwithpython
https://www.w3schools.com/
https://www.101computing.net/pacman-ghost-algorithm/
https://9to5answer.com/how-to-add-a-background-image-into-pygame



'''
#importing libraries
import pygame as p
from random import *
from time import *
#built in libraries
#installed modules/library

#made libraries
from settings import *
from sprites import *



#drawing text function
def draw_text(text, size, color, x, y):
        font_name = p.font.match_font('arial')
        font = p.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)
#npc spawn function
def npc(n):
    for i in range(n):
        m = Npc(randint(0, WIDTH), randint(0, HEIGHT), 25, 25, RED)
        allSprites.add(m)
        allnpcs.add(m)
        
 #deciding if running or not   
running=True
#creating player
player=Player()
allSprites.add(player)
#initializing pygame
p.init()
#creating screen
screen=p.display.set_mode((WIDTH, HEIGHT))
time=p.time.Clock

#NPC class, put it in main because i need to access the player
class Npc(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image=p.Surface((w, h))
        #making npcs salmon
        self.image=p.image.load("R (1) (1).png")
        #self.circle=p.draw.circle()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    #uses angles to find where player is
    def update(self):
        #finding opposite and adjacent angles
        global npcY
        global npcX
        global angle
        opposite=playerY-npcY
        adjacent=playerX-npcX
        angle = m.atan(opposite/adjacent)
        
        #velocity factor
        velocity=1
        nvelocity=-1
        #find player location use sin and cos
        vx = velocity * m.cos(angle)
        vy = velocity * m.sin(angle)
        nvx=nvelocity * m.cos(angle)
        nvy=nvelocity * m.sin(angle)
        #repetitive code, making npcs move away from the player
        if self.rect.x!=WIDTH and player.rect.x>=self.rect.x:
            self.rect.x-=vx
        elif self.rect.x==(WIDTH-30):
            self.rect.x-=nvx
        elif player.rect.x<=self.rect.x:
            self.rect.x-=nvx
        if self.rect.y!=HEIGHT and player.rect.y>=self.rect.y:
            self.rect.y-=vy
        elif self.rect.y==(HEIGHT-30) and player.rect.y<=self.rect.y:
            self.rect.y-=nvy
        if self.rect.y !=NHEIGHT and player.rect.y<=self.rect.y:
            self.rect.y+=vy
        elif self.rect.y==NHEIGHT and player.rect.y>=self.rect.y:
            self.rect.y-=vy
        if self.rect.x!=NWIDTH and player.rect.x<=self.rect.x:
            self.rect.x-=nvx
        elif self.rect.x==NWIDTH and player.rect.x>=self.rect.x:
            self.rect.x-=vx

#background class
class Background(p.sprite.Sprite):
    #initialize class
    def __init__(self, image_file, x, y):
        p.sprite.Sprite.__init__(self)  
        #load image
        self.image = p.image.load(image_file)
        self.rect = self.image.get_rect()
        #set x and y
        self.rect.x=x
        self.rect.y=y




Background("restaurant-png-images-9 (1).png", WIDTH/2, HEIGHT/2)
while running==True:
    if len(allnpcs)<=100:
        npc(1)

    #mob hits
    mobhits = p.sprite.spritecollide(player, allnpcs, True)
    if mobhits:
        SCORE-=1
    for event in p.event.get():
        # check for closed window
        if event.type == p.QUIT:
            running = False
         
        
   
    # updating sprites
    allSprites.update()
    allnpcs.update()

    # drawing background
    screen.fill(BLACK)
   #end of game
    if SCORE>=200:
        draw_text("You've successfully satisfied your hunger! Thank you for dining. Eat 1 more block to exit", 22, WHITE, WIDTH / 2, HEIGHT / 13)
    
     #HOW TO end of game   
    if SCORE==201:
        running=False


      #showing progression  
    draw_text("HUNGER: " + str(SCORE), 22, WHITE, WIDTH / 2, HEIGHT / 24)
    # drawing all sprites
    allSprites.draw(screen)

    # buffer - after drawing everything, flip display
    p.display.flip()

