import pygame
import constants
from sys import exit

# Initiliaze
pygame.init()
screen = pygame.display.set_mode((constants.Width, constants.Height))
pygame.display.set_caption(constants.gameName)
clock = pygame.time.Clock()

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(constants.black)
        
        pygame.display.update()
        clock.tick(60)
    