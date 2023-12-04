from typing import Any
import pygame as pg
from pygame.sprite import Sprite
from pygame.math import Vector2 as vec
import os
from settings import *

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((25, 25))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0) 
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -25
        if keys[pg.K_d]:
            self.acc.x = 25
        if keys[pg.K_w]:
            self.acc.y = -25
        if keys[pg.K_s]:
            self.acc.y = 25
    def update(self):
        self.acc = vec(0,0)
        self.controls()
        # equations of motion
        self.pos += self.acc
        self.rect.midbottom = self.pos
        # prevents player from going off screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class HealthBar():
    def __init__(self, x, y, w, h, max_hp, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp
        self.color = color

    def draw(self, surface):
        #calculate health ratio
        ratio = self.hp / self.max_hp
        pg.draw.rect(surface, (BLACK), (self.x - 6, self.y - 6, self.w + 12, self.h + 12))
        pg.draw.rect(surface, (WHITE), (self.x, self.y, self.w, self.h))
        pg.draw.rect(surface, self.color, (self.x, self.y, self.w * ratio, self.h))

