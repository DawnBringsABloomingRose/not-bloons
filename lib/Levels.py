import pygame
from . import bloon

class Path:
    def __init__(self, waypoints, thickness = 40):
        #waypoints is an array of 2d vectors representing the path, the first element being the start of the path and the last the end
        self.waypoints = waypoints
        self.startpoint = waypoints[0]
        self.thickness = thickness
        self.color = (124, 123, 133) #grey

    def draw_path(self, surface):
        pygame.draw.lines(surface, self.color, False, self.waypoints, self.thickness)


class Level:
    def __init__(self, path, rounds):
        self.path = Path(path)
        self.rounds = rounds
        self.current_round = 0
        self.round = Rounds(rounds[0])


#a round array will consist of some amount of wave arrays
#each wave array will be in the format [wait, time, bloons]
#where wait will be the time in seconds before calling the next wave
#time is the time in frames in between sending each balloon
#and bloons is an array of bloons formatted like [['red', 7], ['blue', 1], ['red', 2]]
class Rounds:
    #put this as a class method in bloon
    BLOON_CLASSES = {
        'red' : bloon.RedBloon,
        'purple' : bloon.PurpleBloon
    }
    def __init__(self, arr):
        self.num_of_waves = len(arr)
        self.wave_counter = 0
        self.bloon_counter = 0
        self.current_wave = arr[0]
        self.waves = arr
        