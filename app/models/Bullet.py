import pygame as pg
import math

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, targetX, targetY):
        pg.sprite.Sprite.__init__(self)

        self.speed      = 1
        self.height     = 6
        self.width      = 3
        self.image      = pg.image.load("images/bullet.png").convert_alpha()
        self.image      = pg.transform.scale(self.image, (self.height, self.width))
        self.rect       = self.image.get_rect()
        self.rect.x     += x
        self.rect.y     += y
        self.position   = pg.Vector2(self.rect.x, self.rect.y)
        self.change_x   = 0
        self.change_y   = 0
        self.walls      = None
        self.original_image = self.image
        distanceX = targetX - self.rect.x
        distanceY = targetX - self.rect.y
        angle = math.atan2(distanceY, distanceX)
        self.dx = math.cos(angle) * self.speed
        self.dy = math.sin(angle) * self.speed
    
    def move(self):
        self.rect.x = self.rect.x + int(self.dx)
        self.rect.y = self.rect.y + int(self.dy)
    
    def update(self):
        self.move()