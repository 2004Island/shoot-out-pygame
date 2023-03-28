import pygame
from background import Background
from sys import exit

pygame.init()
window = pygame.display.set_mode((800, 480))
pygame.display.set_caption('Gun Fight!')
clock = pygame.time.Clock()


class Game:

    def __init__(self):
        self.wildwest = Background(window)
    
    def run(self):
        self.wildwest.update()


game = Game()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    game.run()
    pygame.display.flip()
    clock.tick(60)