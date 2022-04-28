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

pygame.draw.line(screen, blue, (100,200), (300,400), 5)

pygame.draw.rect(screen, red, (100, 200, 50, 100))

pygame.draw.circle(screen, white, (950, 600), 20)

points = (
    (15,20),
    (100,20),
    (819,412),
    (241,529)
)
pygame.draw.polygon(screen, green, points)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()