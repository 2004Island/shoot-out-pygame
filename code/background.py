import pygame

class Background:

    def __init__(self, window):
        self.bg1 = pygame.image.load('graphics/desert_background1.png').convert_alpha()
        self.bg2 = pygame.image.load('graphics/desert_background2.png').convert_alpha()
        self.tick = 0
        self.window = window
    
    def update(self):
        if self.tick < 30:
            self.tick += 1
            self.window.blit(self.bg1, (0,0))
        elif self.tick >= 30 and self.tick < 60:
            self.tick += 1
            self.window.blit(self.bg2, (0,0))
        else:
            self.tick = 0