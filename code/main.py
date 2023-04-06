import pygame
from background import Background
from random import randint
from player import Player
from enemy import Enemy
from sys import exit

pygame.init()
window = pygame.display.set_mode((800, 480))
pygame.display.set_caption('Gun Fight!')
clock = pygame.time.Clock()


class Game:

    def __init__(self):
        self.wildwest = Background(window)
        self.player = Player((200,275), window)
        self.enemey = Enemy((500, 275), window)
        self.current_time_tense = 0
        self.current_time_wait = 0
        self.button_press_time = 0
        self.wait_time = randint(150, 200)
        self.shot = False
    
    def waiting_game(self):
        if self.current_time_wait < self.wait_time:
            self.current_time_wait += 1
        else:
            self.killing_time()
    
    def killing_time(self):
        if self.current_time_tense < 120:
            print("THE ENEMY WILL KILL YOU IF YOU DON'T SHOOT")
            self.current_time_tense += 1
            if self.player.get_input() == 1:
                print(f"You killed him within {self.current_time_tense} ticks")
                self.shot = True
        else:
            if self.shot:
                print("you lived :)")
            else:
                print("you died :(")

    def run(self):
        self.wildwest.update()
        self.player.update()
        self.enemey.update()
        if not self.shot:
            self.waiting_game()
        else:
            print("you lived")


game = Game()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    game.run()
    pygame.display.flip()
    clock.tick(60)