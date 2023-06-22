import pygame
from . import bloon


BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
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
        self.current_round = 1
        self.round = Rounds(rounds[0], self.path)
        self.lives = 100
    
    def update(self, surface):
        basicFont = pygame.font.SysFont(None, 48)
        self.path.draw_path(surface)
        lives_lost = self.round.update(surface)
        self.lives -= lives_lost

        text = basicFont.render('Lives:', True, WHITE, BLUE)
        textRect = text.get_rect()
        textRect.left = 20
        textRect.top = 20
        text = basicFont.render(f'lives: {self.lives}', True, WHITE, BLUE)
        surface.blit(text, textRect)

    def allbloons(self):
        return self.round.spawned_bloons



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
    def __init__(self, arr, path):
        self.num_of_waves = len(arr)
        self.wave_counter = 0
        self.bloon_counter = 0
        self.waves = arr
        self.current_wave = self.waves.pop(0)
        self.spawned_bloons = []
        self.current_bloons = self.current_wave[2][0]
        self.path = path
        self.eor = False

    def update(self, surface):
        self.wave_counter += 1
        self.bloon_counter += 1
        #60 fps
        if not self.eor:
            if self.bloon_counter >= self.current_wave[1] and self.wave_counter >= self.current_wave[0] * 60:
                new_bloon = bloon.classes(self.current_bloons[0])(self.path) #change eventually
                self.spawned_bloons.append(new_bloon)
                self.bloon_counter = 0
                self.current_bloons[1] -= 1
            
            
            if self.current_bloons[1] == 0:
                if len(self.current_wave[2]) == 0:
                    if len(self.waves) != 0:
                        self.current_wave = self.waves.pop(0)
                        self.wave_counter = 0
                    else:
                        self.eor = True
                if not self.eor:
                    self.current_bloons = self.current_wave[2].pop(0)

        lives = 0
        new_bloons = []
        for i in self.spawned_bloons:
            i.update()
            i.draw_bloon(surface)
            if i.startinghealth != i.layer:
                new_bloons.extend(i.spawn_new())
            if i.end:
                lives += i.layer
        self.spawned_bloons.extend(new_bloons)
        self.spawned_bloons = [x for x in self.spawned_bloons if not x.end and not x.destroyed]

        return lives