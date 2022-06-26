import pygame as pg
import math
import config
import app.game.globals as globals
from app.models.tanks.PlayerTurret import PlayerTurret
from app.models.Bullet import Bullet
from app.models.SpriteSheet import SpriteSheet

class PlayerTank(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.height     = config.tank_height
        self.width      = config.tank_width

        # load sprites
        sheet = SpriteSheet('assets/images/tank_base_sprites.png')
        self.right_sprite       = pg.transform.scale(sheet.get_sprite(8, 9, 16, 14), (self.width, self.height))
        self.up_right_sprite    = pg.transform.scale(sheet.get_sprite(40, 9, 16, 14), (self.width, self.height))
        self.up_sprite          = pg.transform.scale(sheet.get_sprite(72, 9, 16, 14), (self.width, self.height))
        self.up_left_sprite     = pg.transform.scale(sheet.get_sprite(104, 9, 16, 14), (self.width, self.height))
        self.left_sprite        = pg.transform.scale(sheet.get_sprite(136, 9, 16, 14), (self.width, self.height))
        self.down_left_sprite   = pg.transform.scale(sheet.get_sprite(168, 9, 16, 14), (self.width, self.height))
        self.down_sprite        = pg.transform.scale(sheet.get_sprite(200, 9, 16, 14), (self.width, self.height))
        self.down_right_sprite  = pg.transform.scale(sheet.get_sprite(232, 9, 16, 14), (self.width, self.height))

        
        self.image      = self.right_sprite 
        self.image      = pg.transform.scale(self.image, (self.height, self.width))
        self.rect       = self.image.get_rect()
        self.rect.x     += x
        self.rect.y     += y
        self.position   = pg.Vector2(self.rect.x, self.rect.y)
        self.change_x   = 0
        self.change_y   = 0
        self.walls      = None
        self.PlayerTurret = PlayerTurret(self.rect.x, self.rect.y)
        self.original_image = self.image
        self.bullets    = []
        self.direction  = 0
        self.angle  = 0

    # Update the player every game loop.
    def update(self):
        self.horizontalCollision()
        self.verticalCollision()
        self.PlayerTurret.setPosition(self)
        self.rotate()

        self.x_centre = (self.rect.x + self.height / 2)
        self.y_centre = (self.rect.y + self.width / 2)
    
    # Handle the change in speed.
    def changeSpeed(self,x,y):

        # if(self.angle == self.direction):
        self.change_x += x
        self.change_y += y
    
    # # Shoot a bullet.
    # def shoot(self):
    #     targetX, targetY = pg.mouse.get_pos()
    #     bullet = Bullet(self.rect.x, self.rect.y, targetX, targetY)
    #     self.bullets.append(bullet) # keep track of how many bullets we've shot
    #     config.all_sprite_list.add(bullet)
    
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
    
    def rotate(self):

        tank_angle = round(self.angle % 360)
        speed = 3

        if(tank_angle > self.direction):
            difference = tank_angle - self.direction
            if(difference < 3):
                pass
            elif(difference > 180):
                 self.angle += speed
            else:
                self.angle -= speed

        else:
            difference = self.direction - tank_angle
            if(difference < 3):
                pass
            elif(difference > 180):
                 self.angle -= speed
            else:
                self.angle += speed

        image_angle = self.angle

        # right
        if(self.angle >= 338 or self.angle < 23):
            self.original_image = self.right_sprite

        # up right
        elif(self.angle >= 23 and self.angle < 68):
            self.original_image = self.up_right_sprite
            image_angle -= 45

        # up
        elif(self.angle >= 68 and self.angle < 113):
            self.original_image = self.up_sprite
            image_angle -= 90

        # up left
        elif(self.angle >= 113 and self.angle < 158):
            self.original_image = self.up_left_sprite
            image_angle -= 135

        # left
        elif(self.angle >= 158 and self.angle < 203):
            self.original_image = self.left_sprite
            image_angle += 180

        # down left
        elif(self.angle >= 203 and self.angle < 248):
            self.original_image = self.down_left_sprite
            image_angle += 135

        # down
        elif(self.angle >= 248 and self.angle < 293):
            self.original_image = self.down_sprite
            image_angle += 90

        # down right
        elif(self.angle >= 293 and self.angle < 338):
            self.original_image = self.down_right_sprite
            image_angle += 45
        
        self.image = pg.transform.rotate(self.original_image, image_angle)
        # self.rect = self.image.get_rect(center=self.position)