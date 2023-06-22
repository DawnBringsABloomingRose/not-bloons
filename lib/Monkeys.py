import pygame, math
import numpy as np

class Monkey:
    def __init__(self, range, attackspeed, image, rect, ammo):
        self.range = range
        self.attackspeed = 60/attackspeed
        self.image = pygame.image.load(image)
        self.rect = rect
        self.rotatedimg = pygame.transform.rotate(self.image, 0)
        self.angle = 0
        self.ammo = ammo
        self.shot_cd = self.attackspeed
        self.shots = []
        self.rotated_image_rect = self.rect
       
    def update(self):
        
        #code to make the rotated image rotate around a point rather than float around
        #why is this so complicated god damn
        pos = self.rect.center
        w, h = self.image.get_size()
        opos = (w/2, h/2)
        image_rect = self.image.get_rect(topleft = (pos[0]-opos[0], pos[1] - opos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
        rotated_offset = offset_center_to_pivot.rotate(-self.angle)
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
        self.rotatedimg = pygame.transform.rotate(self.image, self.angle)
        self.rotated_image_rect = self.rotatedimg.get_rect(center = rotated_image_center)

        self.shot_cd += 1
        
        for shot in self.shots:
            shot.update()
        
        self.shots = [x for x in self.shots if not x.destroyed]
    
    def draw(self, surface):
        self.draw_range(surface)
        surface.blit(self.rotatedimg, self.rotated_image_rect)
        for shot in self.shots:
            shot.draw(surface)

    def draw_range(self, surface):
        pygame.draw.circle(surface,(124, 123, 133, 0.1), self.rect.center, self.range, 5)

    def in_range(self, bloonrects):
        collisions =[]
        axis = [0, 1]
        for bloon in bloonrects:
            x = bloon.center[0] - self.rect.center[0]
            y = bloon.center[1] - self.rect.center[1]
            direction = [x,y]
            magnitude = math.sqrt(pow(direction[0],2) + pow(direction[1], 2))
            if magnitude <= self.range:
                collisions.append(bloon)
        
        if len(collisions) > 0:
            x = collisions[0].center[0] - self.rect.center[0]
            y = collisions[0].center[1] - self.rect.center[1]
            direction = [x,y]
            prod = direction[0]*axis[0] + direction[1]*axis[1]
            magnitude = math.sqrt(pow(direction[0],2) + pow(direction[1], 2))
            angle = prod/magnitude
            magnitude = math.sqrt(pow(axis[0],2) + pow(axis[1], 2))
            angle = angle/magnitude
            angle = np.arccos(angle)
            #self.rotatedimg = pygame.transform.rotate(self.image, np.degrees(angle))
            if x >= 0:
                self.angle = np.degrees(angle)
            else:
                self.angle = 360 - np.degrees(angle)

            if self.shot_cd >= self.attackspeed:
                self.shoot(collisions[0])

    def shoot(self, target):
        ammorect = pygame.Rect(self.rect.x, self.rect.y, 10, 20)
        shot = self.ammo(ammorect, target, self.angle)
        self.shots.append(shot)
        self.shot_cd = 0

class DartMonkey(Monkey):
    def __init__(self, x, y):
        super().__init__(100, 1, "monkey.png", pygame.Rect(x, y, 50, 50), Dart)

        

class Ammo:
    def __init__(self, damage, rect, image, velocity, damagetype, pierce, target, angle):
        self.damage = damage
        self.rect = rect 
        self.image = pygame.image.load(image)
        self.transformedimg = pygame.transform.rotozoom(self.image, angle, 0.2)
        self.velocity = velocity
        self.type = damagetype
        self.pierce = pierce 
        self.target = target
        self.direction = [self.target.center[0] - self.rect.center[0], self.target.center[1] - self.rect.center[1]]
        self.destroyed = False

    def update(self):
        magnitude = math.sqrt(pow(self.direction[0],2) + pow(self.direction[1], 2))
        self.direction[0] = self.direction[0]/magnitude
        self.direction[1] = self.direction[1]/magnitude
        self.rect.bottom += self.direction[1] * self.velocity
        self.rect.left += self.direction[0] * self.velocity

        if self.pierce <= 0:
            self.destroyed = True
    
    def draw(self, surface):
        surface.blit(self.transformedimg, self.rect)

        

class Dart(Ammo):
    def __init__(self, rect, target, angle):
        super().__init__(1, rect, "dart.png", 15, "dart", 3, target, angle)