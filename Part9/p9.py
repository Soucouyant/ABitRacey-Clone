import pygame 
from sys import exit
pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue =(0,0,255)

screen = pygame.display.set_mode((1280,720))
screen.fill(black)

# Shape Drawing
pixArr = pygame.PixelArray(screen)
pixArr[0][0] = green

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()