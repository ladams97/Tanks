import pygame as pg

class KeyPresses():

    @staticmethod
    def update(event, playerTank):
        if event.type == pg.KEYUP:
            KeyPresses.keyUp(event, playerTank)
        
        if event.type == pg.KEYDOWN:
            KeyPresses.keyDown(event, playerTank)
        
        if event.type == pg.MOUSEBUTTONDOWN:
            KeyPresses.mouseButtonDown(event, playerTank)
    
    # When key is pressed down.
    @staticmethod
    def keyDown(event, playerTank):
        match event.key:
            case pg.K_LEFT:
                playerTank.changeSpeed(-3, 0)
                playerTank.direction = 180
            
            case pg.K_a:
                playerTank.changeSpeed(-3, 0)
                playerTank.direction = 180

            case pg.K_RIGHT:
                playerTank.changeSpeed(3, 0)
                playerTank.direction = 0
            
            case pg.K_d:
                playerTank.changeSpeed(3, 0)
                playerTank.direction = 0

            case pg.K_UP:
                playerTank.changeSpeed(0, -3)
                playerTank.direction = 90
            
            case pg.K_w:
                playerTank.changeSpeed(0, -3)
                playerTank.direction = 90
            
            case pg.K_DOWN:
                playerTank.changeSpeed(0, 3)
                playerTank.direction = 270

            case pg.K_s:
                playerTank.changeSpeed(0, 3)
                playerTank.direction = 270
            
           

    # When key is released.
    @staticmethod
    def keyUp(event, playerTank):
        match event.key:
            case pg.K_LEFT:
                playerTank.changeSpeed(3, 0)
            
            case pg.K_a:
                playerTank.changeSpeed(3, 0)

            case pg.K_RIGHT:
                playerTank.changeSpeed(-3, 0)
            
            case pg.K_d:
                playerTank.changeSpeed(-3, 0)

            case pg.K_UP:
                playerTank.changeSpeed(0, 3)
            
            case pg.K_w:
                playerTank.changeSpeed(0, 3)
            
            case pg.K_DOWN:
                playerTank.changeSpeed(0, -3)

            case pg.K_s:
                playerTank.changeSpeed(0, -3)
        
        playerTank.direction = playerTank.angle
    
    # When mouse is pressed down.
    @staticmethod
    def mouseButtonDown(event, playerTank):
        # playerTank.shoot()
        pass