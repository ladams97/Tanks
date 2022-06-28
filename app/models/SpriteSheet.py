import pygame as pg

class SpriteSheet(pg.sprite.Sprite):
    def __init__(self, filename, *groups):
        super().__init__(*groups)
        self.filename = filename
        self.spritesheet = pg.image.load(filename).convert_alpha()

    def get_sprite(self, x, y, w, h):
        sprite = pg.Surface((w, h), pg.SRCALPHA)
        sprite.blit(self.spritesheet, (0, 0), (x, y, w, h))
        return sprite