# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

# Additional notes
# - Further adaptations from https://www.pg.org/wiki/Spritesheet
# - Cleaned up overall formatting.
# - Updated from Python 2 -> Python 3.

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