# Duran Ramlall 
# Pygame Tutorial Set #2 - A Bit Race P1
# Wednesday April 13 2022
# TEJ4M1 P2   
import pygame
from sys import exit

# Initiliaze
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
        pygame.display.update()
        clock.tick(60)
    