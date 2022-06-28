import app.game.globals as globals
import app.menus.pause_menu as pause_menu
import app.models.grid.grid as GameGrid
import pygame as pg
import sys
import config

from app.models.tanks.PlayerTank import PlayerTank

def run(SCREEN):     
    
    clock = pg.time.Clock()
    GameGrid.drawGrid()

    # Player tank.
    playerTank = PlayerTank(config.cell_width, config.cell_height)
    playerTank.walls = globals.wall_list
    globals.all_sprite_list.add(playerTank)
    globals.all_sprite_list.add(playerTank.PlayerTurret)

    # Enemy tank.
    # enemyTank = EnemyTank(600, 600)
    # enemyTank.walls = globals.wall_list
    # globals.all_sprite_list.add(enemyTank)
    # globals.all_sprite_list.add(enemyTank.tankCannon)

    while True:
        
        PLAY_MOUSE_POS = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            else:
                # KeyPresses.update(event, playerTank)
                # KeyPresses.update(event, playerTank)

                if event.type == pg.KEYDOWN:
                    match event.key:
                        case pg.K_ESCAPE:
                            pause_menu.run()
                
        globals.all_sprite_list.update()
        globals.all_sprite_list.draw(SCREEN)

        clock.tick(60)
        pg.display.update()