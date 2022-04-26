import pygame
import constants
import time
import random
from sys import exit

# Initiliaze
pygame.init()
screen = pygame.display.set_mode((constants.Width, constants.Height))
pygame.display.set_caption(constants.gameName)
clock = pygame.time.Clock()

carImg  = pygame.image.load('./Part6/assets/bigGreenCar.png')
roboto = pygame.font.Font('./Part6/assets/Roboto-Black.ttf', 115)

def car(x,y):
    screen.blit(carImg, (x, y))
    
def textObj(text, font):
    textSurface = font.render(text, True, constants.black)
    return textSurface, textSurface.get_rect()

def textDisplay(text):
    TextSurf, TextRect = textObj(text, roboto)
    TextRect.center = ((constants.Width/2),(constants.Height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(2)
    
    gameLoop()
    
def crash():
    textDisplay('You Crashed!')
    
def randomColor():
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    return r,g,b
    
def blockGen(blockX, blockY, blockW, blockH, color):
    pygame.draw.rect(screen, color, [blockX, blockY, blockW, blockH])
    
def gameLoop():
    x = (constants.Width * 0.45)
    y = (constants.Height * 0.627)

    xChange = 0
    carWidth = 150 - 38
    
    blockStartX = random.randrange(0, constants.Width)
    blockStartY = -600
    blockSpeed = 7
    blockWidth = 100
    blockHeight = 100
    
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
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    xChange = 0
                    
        x = x + xChange
        
        
                    
        screen.fill(constants.white)
        blockGen(blockStartX, blockStartY, blockWidth, blockHeight, constants.black)
        blockStartY += blockSpeed
        car(x,y)
        
        if x > constants.Width - carWidth or x < 0:
            crash()
        
        if blockStartY > constants.Height:
            blockStartY = 0 - blockHeight
            blockStartX = random.randrange(0,constants.Width)
            
        pygame.display.update()
        clock.tick(60)
        
# Run Game
gameLoop()



    