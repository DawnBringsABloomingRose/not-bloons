import pygame, math

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (140, 0, 255)
YELLOW = (255, 255, 0)
PINK  = (255, 105, 180)

def classes(value):
    bloon_values = {
        1 : 'red',
        2 : 'blue',
        3 : 'green',
        4 : 'yellow',
        5 : 'pink',
        11 : 'black'
    }

    BLOON_CLASSES = {
        'red' : RedBloon,
        'blue' : BlueBloon,
        'green' : GreenBloon,
        'yellow' : YellowBloon,
        'pink' : PinkBloon,
        'black' : BlackBloon,
        'purple' : PurpleBloon
    }
    if type(value) is int:
        try:
            color = bloon_values[value]
        except:
            return False
        
        return BLOON_CLASSES[color]
    else:
        return BLOON_CLASSES[value]

class Bloon:
    def __init__(self, color, dart_imm, magic_imm, bomb_imm, movement_speed, layers, path):
        base_movement_speed = 4
        self.color = color
        self.dart_imm = dart_imm
        self.magic_imm = magic_imm
        self.bomb_imm = bomb_imm
        self.movespeed = movement_speed * base_movement_speed
        self.layer = layers
        self.path = path
        self.current_waypoint = 1
        self.rect = pygame.Rect(path.startpoint[0], path.startpoint[1], 30, 45)
        self.end = False
        self.immune = []
        self.destroyed = False
        self.classes = classes
        self.startinghealth = layers

    def draw_bloon(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)
        pygame.draw.ellipse(surface, BLACK, self.rect, 1)

    def update(self):
        if self.current_waypoint == len(self.path.waypoints):
            self.end = True
            return
        x = self.path.waypoints[self.current_waypoint][0] - self.rect.left
        y = self.path.waypoints[self.current_waypoint][1] - self.rect.bottom
        direction = [x, y]
        magnitude = math.sqrt(pow(direction[0],2) + pow(direction[1], 2))
        direction[0] = direction[0]/magnitude
        direction[1] = direction[1]/magnitude
        self.rect.bottom += direction[1] * self.movespeed
        self.rect.left += direction[0] * self.movespeed
        if magnitude <= self.movespeed + 2:
            self.current_waypoint += 1

    def damage(self, dart):
        if dart in self.immune or self.immune_to(dart.type):
            return
        self.immune.append(dart)
        self.layer -= dart.damage
        self.destroyed = True
    
    def immune_to (self, dart):
        if dart == 'dart':
            return self.dart_imm
        elif dart == 'bomb':
            return self.bomb_imm
        elif dart == 'magic':
            return self.magic_imm
        else:
            return False
        
    def spawn_new(self):
        to_add = []
        value_to_add = self.layer
        while self.layer > 0:
            new_bloon = self.classes(value_to_add)
            if new_bloon != False:
                self.layer -= value_to_add
                value_to_add = self.layer
                to_add.append(new_bloon)
            else:
                value_to_add -= 1
        bloons = []
        updates = 0
        for bloon in to_add:
            bloon = bloon(self.path)
            bloon.rect.center = self.rect.center
            bloon.current_waypoint = self.current_waypoint
            bloon.immune = self.immune
            for update in range(updates):
                bloon.update()
            updates += 2
            bloons.append(bloon)
        return bloons
        


class PurpleBloon(Bloon):
    def __init__(self, path):
        Bloon.__init__(self, PURPLE, False, True, False, 2, 4, path)

class RedBloon(Bloon):
    def __init__(self, path):
        Bloon.__init__(self, RED, False, False, False, 1, 1, path)

class BlueBloon(Bloon):
    def __init__(self, path):
        Bloon.__init__(self, BLUE, False, False, False, 1.1, 2, path)

class GreenBloon(Bloon):
    def __init__(self, path):
        Bloon.__init__(self, GREEN, False, False, False, 1.3, 3, path)

class YellowBloon(Bloon):
    def __init__(self, path):
        Bloon.__init__(self, YELLOW, False, False, False, 1.5, 4, path)

class PinkBloon(Bloon):
    def __init__(self, path):
        Bloon.__init__(self, PINK, False, False, False, 1.6, 5, path)

class BlackBloon(Bloon):
    def __init__(self, path):
        Bloon.__init__(self, BLACK, False, False, True, 1.8, 11, path)