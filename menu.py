import pygame
import button
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("VADANYA")

game_paused = True
menu_state = "main"
is_menu_open = True

font = pygame.font.SysFont("arialblack", 40)

TEXT_COL = (255, 255, 255)

resume_img = pygame.image.load("assets/images/button_resume.png").convert_alpha()
quit_img = pygame.image.load("assets/images/button_quit.png").convert_alpha()

resume_button = button.Button(304, 125, resume_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#game loop
def menu():
    global is_menu_open, run, screen
    print(screen)
    while is_menu_open:

        screen.fill((52, 78, 91))

        if game_paused == True:
            if menu_state == "main":
                if quit_button.draw(screen):
                    pygame.quit()
                    sys.exit()
                if resume_button.draw(screen):
                    is_menu_open = False
        else:
            draw_text("Press ESC to pause", font, TEXT_COL, 160, 250)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_paused = not game_paused

        pygame.display.update()