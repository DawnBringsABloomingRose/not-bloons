import pygame
import sys
import random
from pygame.locals import *
from lib import bloon, Levels

def update():
    bloons.update()

pygame.init()
mainClock = pygame.time.Clock()

#'settings' variables
WINDOWWIDTH = 800
WINDOWHEIGHT = 800
FPS = 60
basicFont = pygame.font.SysFont(None, 48)
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Not Bloons!')
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


#level and game variables
pathwaypoints = [(0 , WINDOWHEIGHT - 200), (100, WINDOWHEIGHT - 200), (100, 300), (400, 300), (400, 100), (500, 100), (500, WINDOWHEIGHT - 100), (WINDOWWIDTH, WINDOWHEIGHT - 100)]
paths = Levels.Path(pathwaypoints)
bloons = bloon.PurpleBloon(paths)
levels = Levels.Level(paths)
round = 0
lives = 100
money = 800
paused = False

text = basicFont.render('Lives:', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.left = 20
textRect.top = 20

bloons.draw_bloon(windowSurface)
#game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    windowSurface.fill(WHITE)
    bloons.update()
    text = basicFont.render(f'lives: {lives}', True, WHITE, BLUE)
    if bloons.end:
        lives -= bloons.layer
        del bloons
        bloons = bloon.PurpleBloon(paths)
    paths.draw_path(windowSurface)
    bloons.draw_bloon(windowSurface)
    windowSurface.blit(text, textRect)
    pygame.display.update()
    mainClock.tick(FPS)