import pygame
import sys
import random
from pygame.locals import *
from lib import bloon, Levels, Monkeys

def update():
    levels.update(playArea)
    allbloons = levels.allbloons()
    bloonsrect = []
    for i in allbloons:
        bloonsrect.append(i.rect)
    alldarts = []
    for monkey in monkeys:
        monkey.in_range(bloonsrect)
        monkey.update(playArea)
        alldarts.extend(monkey.shots)
    
    if len(selected_monk) > 0:
        mousepos = pygame.mouse.get_pos()
        mouserect = selected_monk[0].get_rect(center = mousepos)
        playArea.blit(selected_monk[0], mouserect)

    for dart in alldarts:
        for i in allbloons:
            if i.rect.colliderect(dart.rect):
                i.damage(dart)
                dart.pierce -= 1

    windowSurface.blit(playArea, playAreaRect)
    windowSurface.blit(buyArea, buyAreaRect)

def updateBuyArea():
    for button in buttons:
        cross_rect = button[0].get_rect(center = button[1].center)
        buyArea.blit(button[0],cross_rect)


pygame.init()
mainClock = pygame.time.Clock()

#'settings' variables
WINDOWWIDTH = 1200
WINDOWHEIGHT = 1000
PLAYAREAWIDTH = WINDOWWIDTH*0.75
PLAYAREAHEIGHT = WINDOWHEIGHT*0.75
BUYAREAWIDTH = PLAYAREAWIDTH/3
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
buyArea = pygame.Surface((BUYAREAWIDTH, PLAYAREAHEIGHT))
buyAreaRect = pygame.Rect(PLAYAREAWIDTH, 0, BUYAREAWIDTH, PLAYAREAHEIGHT)
images = ['monkey.png']
rectsize = (BUYAREAWIDTH, BUYAREAWIDTH/2)
loops = 0
buttons = []
for button in images:
    buttonrect = pygame.Rect((0, (BUYAREAWIDTH/2)*loops), rectsize)
    image = pygame.image.load(button)
    buttons.append([image,buttonrect, Monkeys.DartMonkey])



#level and game variables
pathwaypoints = [(0 , PLAYAREAHEIGHT - 200), (100, PLAYAREAHEIGHT - 200), (100, 300), (400, 300), (400, 100), (500, 100), (500, PLAYAREAHEIGHT - 100), (PLAYAREAWIDTH, PLAYAREAHEIGHT - 100)]
paths = Levels.Path(pathwaypoints)

rounds = []
round1 = [[0, 30, [['red', 3], ['black', 1]]], [3, 10,[['red', 2]]]]
rounds.append(round1)
levels = Levels.Level(pathwaypoints, rounds)
money = 800
paused = False
monkeys = []
monke = Monkeys.DartMonkey(550,200)
selected_monk = []

#pygame.Rect.colliderect(self.rect, bloon)
#game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            if len(selected_monk) > 0:
                new_monk = selected_monk[1](x,y)
                monkeys.append(new_monk)
            for button in buttons:
                if button[1].collidepoint(x-PLAYAREAWIDTH,y):
                    selected_monk = [button[0], button[2]]
    
    windowSurface.fill(WHITE)
    playArea.fill(WHITE)
    buyArea.fill(BLACK)
    if not paused:
        updateBuyArea()
        update()
    pygame.display.update()
    mainClock.tick(FPS)