import pygame

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Bloon:
    def __init__(self, color, dart_imm, magic_imm, bomb_imm, movement_speed, layers):
        base_movement_speed = 4
        self.color = color
        self.dart_imm = dart_imm
        self.magic_imm = magic_imm
        self.bomb_imm = bomb_imm
        self.movement_speed = movement_speed * base_movement_speed
        self.layer = layers

    def draw_bloon(self, surface):
        pygame.draw.ellipse(surface, self.color, ((200,200, 30, 45)))


class PurpleBloon(Bloon):
    def __init__(self):
        Bloon.__init__(self, RED, False, True, False, 2, 4)