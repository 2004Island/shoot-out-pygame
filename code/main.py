import pygame
from sys import exit

pygame.init()
window = pygame.display.set_mode((800, 480))
pygame.display.set_caption('Gun Fight!')
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill((20,20,20))
    pygame.display.flip()
    clock.tick(60)