import pygame


class Player:

    def __init__(self, pos, window):
        self.pos = pos
        self.idle1 = pygame.image.load("graphics/guy1.png")
        self.idle2 = pygame.image.load('graphics/guy2.png')
        self.tick = 0
        self.fire = False
        self.window = window

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            return 1
    
    def update(self):
        if self.tick < 30:
            self.tick += 1
            self.window.blit(self.idle1, self.pos)
        elif self.tick >= 30 and self.tick < 60:
            self.tick += 1
            self.window.blit(self.idle2, self.pos)
        else:
            self.tick = 0