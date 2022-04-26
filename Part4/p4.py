import pygame
import constants
from sys import exit

# Initiliaze
pygame.init()
screen = pygame.display.set_mode((constants.Width, constants.Height))
pygame.display.set_caption(constants.gameName)
clock = pygame.time.Clock()

carImg  = pygame.image.load('./Part4/assets/bigGreenCar.png')

def car(x,y):
    screen.blit(carImg, (x, y))
    
x = (constants.Width * 0.45)
y = (constants.Height * 0.8)

xChange = 0
yChange = 0
carSpeed = 0

carWidth = 150 - 38

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Movement Handler
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xChange = -5
            if event.key == pygame.K_RIGHT:
                xChange = 5
            if event.key == pygame.K_UP:
                yChange = -5
            if event.key == pygame.K_DOWN:
                yChange = 5
        if event.type == pygame.KEYUP:
            xChange = 0
            yChange = 0
        
    x = x + xChange
    y = y + yChange

                    
    screen.fill(constants.white)
    car(x,y)
        
    if x > constants.Width - carWidth or x < 0:
        pygame.quit()
        exit()
        
    pygame.display.update()
    clock.tick(60)
    