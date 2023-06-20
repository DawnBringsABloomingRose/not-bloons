import pygame

class Path:
    def __init__(self, waypoints, thickness = 40):
        #waypoints is an array of 2d vectors representing the path, the first element being the start of the path and the last the end
        self.waypoints = waypoints
        self.startpoint = waypoints[0]
        self.thickness = thickness
        self.color = (124, 123, 133) #grey

    def draw_path(self, surface):
        pygame.draw.lines(surface, self.color, False, self.waypoints, self.thickness)