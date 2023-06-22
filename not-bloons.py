import pygame
import sys
import random
from pygame.locals import *
from lib import bloon, Levels, Monkeys

def update():
    levels.update(playArea)
    allbloons = levels.allbloons()
    bloonsrect = []
    windowSurface.blit(playArea, playAreaRect)
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
WINDOWWIDTH = 1200
WINDOWHEIGHT = 1000
PLAYAREAWIDTH = WINDOWWIDTH*0.75
PLAYAREAHEIGHT = WINDOWHEIGHT*0.75
FPS = 60
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
basicFont = pygame.font.SysFont(None, 48)
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Not Bloons!')
playArea = pygame.Surface((WINDOWWIDTH*0.75, WINDOWHEIGHT*0.75))
playAreaRect = pygame.Rect(0, 0, WINDOWHEIGHT * 0.75, WINDOWWIDTH*0.75)


#level and game variables
pathwaypoints = [(0 , PLAYAREAHEIGHT - 200), (100, PLAYAREAHEIGHT - 200), (100, 300), (400, 300), (400, 100), (500, 100), (500, PLAYAREAHEIGHT - 100), (PLAYAREAWIDTH, PLAYAREAHEIGHT - 100)]
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

    playArea.fill(WHITE)
    if not paused:
        monke.update(playArea)
        update()
    pygame.display.update()
    mainClock.tick(FPS)