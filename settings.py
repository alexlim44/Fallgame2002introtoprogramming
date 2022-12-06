import pygame as p

WIDTH=1100
HEIGHT=900

screen=p.display.set_mode((WIDTH, HEIGHT))

PLAYER_GRAV = 0.4
PLAYER_FRIC = .1
SCORE = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS=30

def draw_text(text, size, color, x, y):
        font_name = p.font.match_font('arial')
        font = p.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)