import config
import pygame as pg
from app.models.grid.cells.Cell import Cell

class BlockCell(Cell):

    def __init__(self, x, y):
 
        self.image = pg.image.load("assets/images/tiles/block.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (config.cell_width, config.cell_sprite_height))
        self.rect = pg.transform.scale(self.image, (config.cell_width, config.cell_height)).get_rect()

        self.sprite_rect = self.rect.copy()
        self.sprite_rect.bottom = self.image.get_rect().bottom

        self.collideRect =  pg.rect.Rect((0, 0), (32, 150))

        print("sprite: ", self.sprite_rect)
        print("rect: ", self.rect)

        # debugging - highlights borders of grids
        pg.draw.rect(self.image, (config.red), self.rect, 2) # rect
        pg.draw.rect(self.image, (config.yellow), self.sprite_rect, 3) # image rect

        Cell.__init__(self, x, y)