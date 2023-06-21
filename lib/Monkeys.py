import pygame

class Monkey:
    def __init__(self, range, attackspeed, image, rect, ammo):
        self.range = range
        self.attackspeed = attackspeed
        self.image = pygame.image.load(image)
        self.rect = rect
        self.rotatedimg = pygame.transform.rotate(self.image, 0)
        self.ammo = ammo
       
    def update(self, surface):
        self.draw_range(surface)
        surface.blit(self.rotatedimg, self.rect)
    
    def draw_range(self, surface):
        pygame.draw.circle(surface,(124, 123, 133, 0.1), self.rect.center, self.range, 5)

class DartMonkey(Monkey):
    def __init__(self, x, y):
        super().__init__(100, 1, "monkey.png", pygame.Rect(x, y, 50, 50), Dart)

        

class Ammo:
    def __init__(self, damage, rect, image, velocity, damagetype, pierce, target):
        self.damage = damage
        self.rect = rect 
        self.image = image
        self.velocity = velocity
        self.type = damagetype
        self.pierce = pierce 
        self.target = target

class Dart(Ammo):
    def __init__(self, rect, target):
        super().__init__(1, rect, "dart.png", 10, "dart", 3, target)