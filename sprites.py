from pygame.sprite import Sprite
import pygame as p
from settings import *
import random
from math import atan, cos, sin, atan2
vec=p.math.Vector2


playerY=30
npcY=10
playerX=30
npcX=30


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
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.health = 10
    def controls(self):
        keys = p.key.get_pressed()
        if keys[p.K_w]:
            self.acc.y = -5
        if keys[p.K_a]:
            self.acc.x = -5
        if keys[p.K_s]:
            self.acc.y = 5
        if keys[p.K_d]:
            self.acc.x = 5
    def update(self):
        self.controls()
        # friction
        self.acc.x += self.vel.x * -0.1
        self.acc.y += self.vel.y * -0.1
        self.pos += self.vel + 0.1 * self.acc
        self.rect.midbottom = self.pos

class Npc(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        Sprite.image=p.surface((10, 10))
        r=random.randint(0,225)
        g=random.randint(0,225)
        b=random.randint(0,225)
        self.image.fill((r, g, b))
        self.circle=p.draw.circle()
        self.pos = vec(WIDTH/2, HEIGHT-45)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    #uses angles to find where player is
    def update(self):
        #finding opposite and adjacent angles
        opposite=playerY-npcY
        adjacent=playerX-npcX
        angle = atan(opposite/adjacent)
        #make npcs turn around if behind
        '''if npcX>playerX:
            angle=angle-180'''
        velocity=3 
        #find player location
        vx = velocity * cos(angle)
        vy = velocity * sin(angle)
        #make npcs run away
        npcX = npcX - vx
        npcY = npcY - vy
allSprites=p.sprite.Group()
allnpcs=p.sprite.Group()



