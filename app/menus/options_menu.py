import pygame as pg
import sys

from app.models.Button import Button as Button

def run(SCREEN):
    run = True

    while run:
        OPTIONS_MOUSE_POS = pg.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = pg.font.Font("assets/fonts/font.ttf", 100).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        backToMenuButton = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=pg.font.Font("assets/fonts/font.ttf", 100), base_color="Black", hovering_color="Green")

        backToMenuButton.changeColor(OPTIONS_MOUSE_POS)
        backToMenuButton.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if backToMenuButton.checkForInput(OPTIONS_MOUSE_POS):
                    run = False

        pg.display.update()