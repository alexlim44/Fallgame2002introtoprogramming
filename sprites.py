from pygame.sprite import Sprite
import pygame as p
from settings import *
vec=p.math.Vector2




class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        Sprite.image=p.surface((30, 30))
        r=143
        g=211
        b=210
        self.image.fill((r, g, b))
        self.rect=self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT-45)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.health = 10
        