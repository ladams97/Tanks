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
        self.up_right_sprite    = pg.transform.scale(sheet.get_sprite(38, 6, 19, 19), (self.width, self.height))
        self.up_sprite          = pg.transform.scale(sheet.get_sprite(72, 9, 16, 14), (self.width, self.height))
        self.up_left_sprite     = pg.transform.scale(sheet.get_sprite(102, 6, 19, 19), (self.width, self.height))
        self.left_sprite        = pg.transform.scale(sheet.get_sprite(136, 9, 16, 14), (self.width, self.height))
        self.down_left_sprite   = pg.transform.scale(sheet.get_sprite(166, 6, 19, 19), (self.width, self.height))
        self.down_sprite        = pg.transform.scale(sheet.get_sprite(200, 9, 16, 14), (self.width, self.height))
        self.down_right_sprite  = pg.transform.scale(sheet.get_sprite(230, 6, 19, 19), (self.width, self.height))

        
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
        self.detectInput()
        self.horizontalCollision()
        self.verticalCollision()
        self.PlayerTurret.setPosition(self)
        self.x_centre = (self.rect.x + self.height / 2)
        self.y_centre = (self.rect.y + self.width / 2)
        self.rotate()
        pg.draw.rect(self.image, (config.red), self.rect, 2)
    
    # Handle the change in speed.
    def move(self,x,y):
        self.change_x = x
        self.change_y = y

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
    
    # rotate tank
    def rotate(self):

        current_angle = round(self.angle % 360)
        speed = 3
        
        if(current_angle > self.direction):
            difference = current_angle - self.direction
            if(difference < 3):
                pass
            elif(difference > 180):
                current_angle += speed
            else:
                current_angle -= speed

        else:
            difference = self.direction - current_angle
            if(difference < 3):
                pass
            elif(difference > 180):
                current_angle -= speed
            else:
                current_angle += speed
        
        self.angle = current_angle

        # right
        if(self.angle >= 338 or self.angle < 23):
            self.original_image = self.right_sprite

        # up right
        if(self.angle >= 23 and self.angle < 68):
            self.original_image = self.up_right_sprite

        # up
        if(self.angle >= 68 and self.angle < 113):
            self.original_image = self.up_sprite

        # up left
        if(self.angle >= 113 and self.angle < 158):
            self.original_image = self.up_left_sprite

        # left
        if(self.angle >= 158 and self.angle < 203):
            self.original_image = self.left_sprite

        # down left
        if(self.angle >= 203 and self.angle < 248):
            self.original_image = self.down_left_sprite

        # down
        if(self.angle >= 248 and self.angle < 293):
            self.original_image = self.down_sprite

        # down right
        if(self.angle >= 293 and self.angle < 338):
            self.original_image = self.down_right_sprite

        self.image = self.original_image
    
    # detect input from the player
    def detectInput(self):

        keys = pg.key.get_pressed()

        # up right
        if (keys[pg.K_UP] and keys[pg.K_RIGHT]) or (keys[pg.K_w] and keys[pg.K_d]):
            self.direction = 45
            self.move(3, -3)
        
        # up left
        elif (keys[pg.K_UP] and keys[pg.K_LEFT]) or (keys[pg.K_w] and keys[pg.K_a]):
            self.direction = 135
            self.move(-3, -3)

        # down left
        elif (keys[pg.K_DOWN] and keys[pg.K_LEFT]) or (keys[pg.K_s] and keys[pg.K_a]):
            self.direction = 225
            self.move(-3, 3)

        # down right
        elif (keys[pg.K_DOWN] and keys[pg.K_RIGHT]) or (keys[pg.K_s] and keys[pg.K_d]):
            self.direction = 315
            self.move(3, 3)
        
        # left
        elif (keys[pg.K_LEFT]) or (keys[pg.K_a]):
            self.direction = 180
            self.move(-3, 0)
        
        # right
        elif (keys[pg.K_RIGHT]) or (keys[pg.K_d]):
            self.direction = 0
            self.move(3, 0)

        # up
        elif (keys[pg.K_UP]) or (keys[pg.K_w]):
            self.direction = 90
            self.move(0, -3)
        
        # down
        elif (keys[pg.K_DOWN]) or (keys[pg.K_s]):
            self.direction = 270
            self.move(0, 3)
        
        # no movement
        else:
            self.direction = self.angle
            self.move(0, 0)
            