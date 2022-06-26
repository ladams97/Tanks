import pygame as pg
import sys
import app.game.play as play
import app.menus.options_menu as options_menu
from app.models.Button import Button as Button

def run(SCREEN):
    BACKGROUND = pg.image.load("assets/images/Background.png")
    MENU_FONT = pg.font.Font("assets/fonts/font.ttf", 100)
    MENU_BUTTON_FONT = pg.font.Font("assets/fonts/font.ttf", 75)

    while True:
        SCREEN.blit(BACKGROUND, (0, 0))

        MENU_MOUSE_POS = pg.mouse.get_pos()

        MENU_TEXT = MENU_FONT.render("TANKS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pg.image.load("assets/images/play_button.png"), pos=(640, 250), 
                            text_input="PLAY", font=MENU_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")

        OPTIONS_BUTTON = Button(image=pg.image.load("assets/images/options_button.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=MENU_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Button(image=pg.image.load("assets/images/quit_button.png"), pos=(640, 550), 
                            text_input="QUIT", font=MENU_BUTTON_FONT, base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play.run(SCREEN)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options_menu.run(SCREEN)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.update()