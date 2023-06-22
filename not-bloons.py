import pygame
import sys
import random
from pygame.locals import *
from lib import bloon, Levels, Monkeys

def update():
    levels.update(windowSurface)
    allbloons = levels.allbloons()
    bloonsrect = []
    for i in allbloons:
        bloonsrect.append(i.rect)
    monke.in_range(bloonsrect)
    for dart in monke.shots:
        for i in allbloons:
            if i.rect.colliderect(dart.rect):
                i.damage(dart)
                dart.pierce -= 1

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

rounds = []
round1 = [[0, 30, [['red', 3], ['black', 1]]], [3, 10,[['red', 2]]]]
rounds.append(round1)
levels = Levels.Level(pathwaypoints, rounds)
money = 800
paused = False

monke = Monkeys.DartMonkey(550,200)

#pygame.Rect.colliderect(self.rect, bloon)
#game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    windowSurface.fill(WHITE)
    if not paused:
        monke.update(windowSurface)
        update()
    pygame.display.update()
    mainClock.tick(FPS)