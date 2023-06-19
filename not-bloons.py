import pygame
import sys
import random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()


WINDOWWIDTH = 800
WINDOWHEIGHT = 800
FPS = 60
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Not Bloons!')


#add to seperate module and import
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



#game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(WHITE)
    pygame.display.update()
    mainClock.tick(60)