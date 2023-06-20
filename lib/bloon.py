import pygame, math

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (140, 0, 255)

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

    def draw_bloon(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)

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
        


class PurpleBloon(Bloon):
    def __init__(self, path):
        Bloon.__init__(self, PURPLE, False, True, False, 2, 4, path)

class RedBloon(Bloon):
    def __init__(self, path):
        Bloon.__init__(self, RED, False, False, False, 1, 1, path)