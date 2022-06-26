import pygame as pg
import config

class EnemyTank(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.height     = 50
        self.width      = 50
        self.image      = config.playerTank
        self.image      = pg.transform.scale(self.image, (self.height, self.width))
        self.rect       = self.image.get_rect()
        self.rect.x     += x
        self.rect.y     += y
        self.position   = pg.Vector2(self.rect.x, self.rect.y)
        self.change_x   = 0
        self.change_y   = 0
        self.walls      = None
        self.tankCannon = TankCannon(self.rect.x, self.rect.y)
        self.original_image = self.image

    # Update the player every game loop.
    def update(self):
        self.horizontalCollision()
        self.verticalCollision()
        self.tankCannon.setPosition(self)
    
    # Handle the change in speed.
    def changeSpeed(self,x,y):
        self.change_x += x
        self.change_y += y
    
    # Detect hortizontal collisions.
    def horizontalCollision(self):
        self.rect.x += self.change_x
        block_hit_list = pg.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
    
    # Detect vertical collisions.
    def verticalCollision(self):
        self.rect.y += self.change_y
        block_hit_list = pg.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class TankCannon(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.width = 50
        self.height = 50
        self.image = config.playerCannon
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.original_image = self.image
        
        self.rect = self.image.get_rect()
        self.rect.x += x
        self.rect.y += y
        self.position = pg.Vector2(self.rect.x, self.rect.y)
        self.angle = 0
    
    # Update every game loop.
    def update(self):
        pass
    
    # Set the tank cannon position.
    def setPosition(self, tank):
        tankCenter = tank.rect.x + tank.height / 2, tank.rect.y + tank.width / 2
        self.position = pg.Vector2(tankCenter)
        self.rotate()

    # Rotate the sprite to face the cursor
    def rotate(self):
        self.angle += 1
        self.image = pg.transform.rotate(self.original_image, int(self.angle))
        self.rect = self.image.get_rect(center=self.position)