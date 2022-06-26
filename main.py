# don't generate __pycache__ for imports
import sys
sys.dont_write_bytecode = True

# imports
import app.menus.main_menu as main_menu
import pygame as pg

# run
pg.init()
pg.display.set_caption("Tanks")

SCREEN = pg.display.set_mode((1280, 720))

def main():
    main_menu.run(SCREEN)

main()