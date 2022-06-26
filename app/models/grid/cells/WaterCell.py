import config
import pygame as pg
from app.models.grid.cells.Cell import Cell

class WaterCell(Cell):

    def __init__(self, x, y):

        self.image = pg.image.load("assets/images/tiles/water.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (config.cell_width, config.cell_height))
        self.rect = self.image.get_rect()

        Cell.__init__(self, x, y)