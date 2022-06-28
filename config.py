import pygame as pg

# Dimensions.
width   = 1680
height  = 1200
screen = pg.display.set_mode([width, height])
scale = 8

cell_width = 16 * scale
cell_height = 12 * scale
cell_sprite_height = cell_height * 2

tank_width = 16 * scale
tank_height = 14 * scale

tank_turret_width = 20 * scale
tank_turret_height = 20 * scale

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