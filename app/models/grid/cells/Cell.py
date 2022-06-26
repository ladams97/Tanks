import config
import pygame as pg

class Cell(pg.sprite.Sprite):

    def __init__(self, x, y):

        pg.sprite.Sprite.__init__(self)

        self.rect.x = x
        self.rect.y = y