import pygame as pg
import config
import math
from app.models.SpriteSheet import SpriteSheet

class PlayerTurret(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.width = 133
        self.height = 133

        sheet = SpriteSheet('assets/images/tank_cannon_sprites.png')
        self.right_sprite       = pg.transform.scale(sheet.get_sprite(5, 4, 24, 25), (self.width, self.height))
        self.up_right_sprite    = pg.transform.scale(sheet.get_sprite(37, 4, 24, 25), (self.width, self.height))
        self.up_sprite          = pg.transform.scale(sheet.get_sprite(69, 4, 24, 25), (self.width, self.height))
        self.up_left_sprite     = pg.transform.scale(sheet.get_sprite(101, 4, 24, 25), (self.width, self.height))
        self.left_sprite        = pg.transform.scale(sheet.get_sprite(133, 4, 24, 25), (self.width, self.height))
        self.down_left_sprite   = pg.transform.scale(sheet.get_sprite(162, 4, 24, 25), (self.width, self.height))
        self.down_sprite        = pg.transform.scale(sheet.get_sprite(195, 4, 24, 25), (self.width, self.height))
        self.down_right_sprite  = pg.transform.scale(sheet.get_sprite(227, 4, 24, 25), (self.width, self.height))

        self.image = self.right_sprite 
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.original_image = self.image
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.x += x
        self.rect.y += y
        self.x_centre = (self.rect.x + self.height)
        self.y_centre = (self.rect.y + self.width)
        self.position = pg.Vector2(self.rect.x, self.rect.y)

    
    # Update every game loop.
    def update(self):
        pass
    
    # Set the tank cannon position.
    def setPosition(self, tank):
        tankCenter = (tank.rect.x + tank.height / 2), (tank.rect.y + tank.width / 2)
        self.position = pg.Vector2(tankCenter)
        self.rotate()

    # Rotate the sprite to face the cursor
    def rotate(self):
        mouse_x, mouse_y = pg.mouse.get_pos()

        self.x_centre = (self.rect.x + self.height / 2)
        self.y_centre = (self.rect.y + self.width / 2)

        rel_x, rel_y = mouse_x - self.x_centre, mouse_y - self.y_centre

        cursor_angle = round((-math.atan2(rel_y, rel_x) * (180 / math.pi)) % 360)
        cannon_angle = round(self.angle % 360)

        speed = 3

        if(cannon_angle > cursor_angle):
            difference = cannon_angle - cursor_angle
            if(difference < 3):
                pass
            elif(difference > 180):
                 self.angle += speed
            else:
                self.angle -= speed

        else:
            difference = cursor_angle - cannon_angle
            if(difference < 3):
                pass
            elif(difference > 180):
                 self.angle -= speed
            else:
                self.angle += speed
        
        image_angle = self.angle
        
        # right
        if(cannon_angle >= 338 or cannon_angle < 23):
            self.original_image = self.right_sprite

        # up right
        elif(cannon_angle >= 23 and cannon_angle < 68):
            self.original_image = self.up_right_sprite
            image_angle -= 45

        # up
        elif(cannon_angle >= 68 and cannon_angle < 113):
            self.original_image = self.up_sprite
            image_angle -= 90

        # up left
        elif(cannon_angle >= 113 and cannon_angle < 158):
            self.original_image = self.up_left_sprite
            image_angle -= 135

        # left
        elif(cannon_angle >= 158 and cannon_angle < 203):
            self.original_image = self.left_sprite
            image_angle += 180

        # down left
        elif(cannon_angle >= 203 and cannon_angle < 248):
            self.original_image = self.down_left_sprite
            image_angle += 135

        # down
        elif(cannon_angle >= 248 and cannon_angle < 293):
            self.original_image = self.down_sprite
            image_angle += 90

        # down right
        elif(cannon_angle >= 293 and cannon_angle < 338):
            self.original_image = self.down_right_sprite
            image_angle += 45

        
        self.image = pg.transform.rotate(self.original_image, image_angle)
        self.rect = self.image.get_rect(center=self.position)