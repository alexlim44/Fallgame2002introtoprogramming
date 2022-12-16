#libraries
from pygame.sprite import Sprite
import pygame as p
from settings import *
import random
import math as m
from pygame.locals import *
p.init()
#whole bunch of setup for the NPCs, player and npc starting position
vec=p.math.Vector2
global npcY
playerY=HEIGHT/2
npcY=HEIGHT/random.randint(3, 7)
playerX=WIDTH/2
npcX=WIDTH/random.randint(3, 7)



#player class
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        #making player albania (eagle)
        self.image=p.Surface((30, 30))
        self.image=p.image.load("758454.png")
        self.rect=self.image.get_rect()
        #centering sprite
        self.rect.center = (WIDTH/2, HEIGHT/2)
        #positioning
        self.pos = vec(playerX, playerY)
        #velocity/acceleration
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        

    def controls(self):
        #self.pos=self.pos-mouseX
        keys = p.key.get_pressed()
        #had to get repetitive to fix the movement
        if keys[p.K_w] and self.rect.x!=NHEIGHT:
            self.acc.y = -5
            self.acc.x=0
        elif self.rect.y==(NHEIGHT):
            self.acc.y=.1
        if keys[p.K_a] and self.rect.x!=NWIDTH:
            self.acc.x = -5
            self.acc.y=0
        elif self.rect.x==NWIDTH:
            self.acc.x=.1
        if keys[p.K_s] and self.rect.y!=HEIGHT:
            self.acc.y = 5
            self.acc.x=0
        elif self.rect.y==(HEIGHT-30):
            self.acc.y=-.1
        if keys[p.K_d] and self.rect.x!=WIDTH:
            self.acc.x=5
            self.acc.y=0
        elif self.rect.x==(WIDTH-30):
            self.acc.x=-.1
    

    def update(self):
        self.controls()
        # friction
        self.acc.x += self.vel.x * -0.1
        self.acc.y += self.vel.y * -0.1
        self.pos += self.vel + 0.1 * self.acc
        self.rect.midbottom = self.pos


        
        

#creating groups
allSprites=p.sprite.Group()
allnpcs=p.sprite.Group()



