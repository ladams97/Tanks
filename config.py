import pygame as pg

# Dimensions.
width   = 1680
height  = 1200
screen = pg.display.set_mode([width, height])

cell_width = 128
cell_height = 96
cell_sprite_height = cell_height * 2

tank_width = 128
tank_height = 112

# Colours.
black       = (0  , 0  , 0  )
white       = (255, 255, 255)
blue        = (50 , 50 , 255)
green       = (0  , 102, 0  )
calm_blue   = (52 , 78 , 91 )
sand        = (245, 217, 154)
brown       = (177, 114, 79 )
water       = (123, 209, 226)
red         = (255, 0  , 0  )
yellow      = (255, 255, 0  )