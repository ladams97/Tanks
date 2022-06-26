import pygame as pg
import sys

def run():
    game_paused = True
    while game_paused:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                match event.key:
                    case pg.K_ESCAPE:
                        game_paused = False