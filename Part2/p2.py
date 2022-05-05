



import pygame
import constants
from sys import exit

# Initiliaze
pygame.init()
screen = pygame.display.set_mode((constants.Width, constants.Height))
pygame.display.set_caption(constants.gameName)
clock = pygame.time.Clock()

carImg  = pygame.image.load('./Part2/assets/bigGreenCar.png')

def car(x,y):
    screen.blit(carImg, (x, y))
    
x = (constants.Width * 0.4)
y = (constants.Height * 0.6)

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(constants.white)
        car(x,y)
        
        pygame.display.update()
        clock.tick(60)
    