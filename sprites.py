from pygame.sprite import Sprite
import pygame as p
from settings import *
import random
from math import atan, cos, sin
vec=p.math.Vector2


playerY=30
npcY=10
playerX=30
npcX=30


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        Sprite.image=p.surface((10, 10))
        r=143
        g=211
        b=210
        self.image.fill((r, g, b))
        self.rect=self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT-45)
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
        self.health = 1
    def update(self):
        opposite=playerY-npcY
        adjacent=playerX-npcX
        angle = atan(opposite/adjacent)
        if npcX>playerX:
            angle=angle+180
        velocity=3 
        vx = velocity * cos(angle)
        vy = velocity * sin(angle)
        npcX = npcX - vx
        npcY = npcY - vy



