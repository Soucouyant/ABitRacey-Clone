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

carImg  = pygame.image.load('./Part15/assets/bigGreenCar.png')
roboto = pygame.font.Font('./Part15/assets/Roboto-Black.ttf', 27)

def exitGame():
    pygame.quit()
    exit()

def blocksDodged(count):
    text = roboto.render("Dodged: "+str(count), True, constants.black)
    screen.blit(text, (0,0)) 

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
    
# Add params
def buttons(msg,x,y,w,h,ic,ac,action=None):
    # Mouse Pos
    mousePos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    # Change in Color
    if x+w > mousePos[0] > x and y+h > mousePos[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        if click[0] == True:
            action()
    else: 
        pygame.draw.rect(screen, ic, (x,y,w,h))
        
    # Button Text
    textSurf, textRect = textObj(msg, roboto)
    textRect.center = (
        (x+(w/2)),
        (y+(h/2))
    )
    screen.blit(textSurf,textRect)

# def randomColor():
#     r = random.randrange(0,255)
#     g = random.randrange(0,255)
#     b = random.randrange(0,255)
#     return r,g,b

def blockGen(blockX, blockY, blockW, blockH, color):
    pygame.draw.rect(screen, color, [blockX, blockY, blockW, blockH])
    
def splashScreen():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                exitGame()
                
        screen.fill(constants.white)
        TextSurf, TextRect = textObj("A bit Racey", roboto)
        TextRect.center = ((constants.Width/2), (constants.Height/2.5))
        screen.blit(TextSurf, TextRect)
        
        # Button Function Calls
        buttons("GO!", 150,350,100,50,constants.green,constants.lightGreen,gameLoop)
        buttons("Exit",550,350,100,50,constants.red,constants.lightRed,exitGame)
        
        pygame.display.update()
        clock.tick(15)
    
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
    
    blockCount = 1
    dodged = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame()

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
        
        blockStartY += blockSpeed
        blocksDodged(dodged)
        
        if x > constants.Width - carWidth or x < 0:
            crash()
            
        if blockStartY > constants.Height:
            blockStartY = 0 - blockHeight
            blockStartX = random.randrange(0,constants.Width)
            dodged += 1
            blockSpeed += .15
            blockWidth += (dodged * 1.2)
        
        if y < blockStartY+blockHeight:  
            if x > blockStartX and x < blockStartX+blockWidth or x+carWidth > blockStartX and x + carWidth < blockStartX + blockWidth:
                crash()
            
       
        pygame.display.update()
        clock.tick(60)
        
# Run Game
splashScreen()
gameLoop()