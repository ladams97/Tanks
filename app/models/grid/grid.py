import config as config
import app.game.globals as globals
from app.models.grid.cells.GroundCell import GroundCell
from app.models.grid.cells.BlockCell import BlockCell
from app.models.grid.cells.BlockCellTop import BlockCellTop
from app.models.grid.cells.WaterCell import WaterCell
import csv

ground  = 0
block   = 1
water   = 2

level_csv = 'levels/main/1.csv'
width = config.cell_width
height = config.cell_height

# Draw a grid on screen.
def drawGrid():
    grid = turnCsvIntoArray(level_csv)
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            col = int(col)
            drawTile(col, col_index, row_index, width, height)

# Draw a tile on screen.
def drawTile(col, col_index, row_index, width, height):
    if(col == 0):
        ground_tile = GroundCell(col_index * width, row_index * height)
        globals.all_sprite_list.add(ground_tile)
    elif(col == 1):
        block_tile = BlockCell(col_index * width, row_index * height)
        block_top = BlockCellTop(col_index * width, (row_index * height) - config.cell_height)
        globals.wall_list.add(block_tile)
        globals.all_sprite_list.add(block_tile)
        globals.all_sprite_list.add(block_top)
    elif(col == 2):
        water_tile = WaterCell(col_index * width, row_index * height)
        globals.wall_list.add(water_tile)
        globals.all_sprite_list.add(water_tile)
            

# Turn our level.csv into a multidimensional list.
def turnCsvIntoArray(level_csv):
    return list(csv.reader(open(level_csv)))