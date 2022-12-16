from pygame.sprite import Sprite
import pygame as p
from settings import *
import random
import math as m
#import processing_py as py
#from processing_py import *
import sys
from pygame.locals import *
p.init()

vec=p.math.Vector2
global npcY
mouseX, mouseY=p.mouse.get_pos()
playerY=HEIGHT/2
npcY=HEIGHT/random.randint(3, 7)
playerX=WIDTH/2
npcX=WIDTH/random.randint(3, 7)




class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image=p.Surface((30, 30))
        r=143
        g=211
        b=210
        self.image.fill(GREEN)
        self.rect=self.image.get_rect()
        
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(playerX, playerY)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.health = 10

    def controls(self):
        #self.pos=self.pos-mouseX
        keys = p.key.get_pressed()
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


        
        


allSprites=p.sprite.Group()
allnpcs=p.sprite.Group()



