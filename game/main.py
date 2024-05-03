# Game Colour Palette: https://colorhunt.co/palette/11009e4942e4e6b9defae7f3

import os
import sys
import pygame
import asyncio
import random

#PyGame initialisation
pygame.init()
pygame.font.init()

# Variable Declaration
SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
caption = pygame.display.set_caption("Whack-a-Duck")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Calibri", 40)
running = True
gameState = "start"
mousePos = 0
cells = []
circles = []
score = 0

timer = 20
timerInterval = 1000
timerEvent = pygame.USEREVENT + 1
pygame.time.set_timer(timerEvent, timerInterval)
timerText = font.render("Time: " + str(timer), False, [0,0,0])

async def main():
    global screen, clock, timer, running, mousePos, timerText
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
            elif event.type == timerEvent:
                timer -= 1
                timerText = font.render("Time: " + str(timer), False, [0,0,0])
                if timer == 0:
                    pygame.time.set_timer(timerEvent, 0)

        if gameState == "start":
            titleScreen(mousePos)
        elif gameState == "instructions":
            instructionScreen()
        elif gameState == "setup":
            drawGrid()
        elif gameState == "game":
            gameLogic(mousePos)
        elif gameState == "exit":
            pygame.quit()
            sys.exit()
    
        pygame.display.flip()
        clock.tick(30)

        await asyncio.sleep(0)

    pygame.quit()


def titleScreen(mousePos):
    global screen, gameState

    # Fills screen with colour
    screen.fill("#11009E")

    # TODO: Remove game/ from path before packaging with pygbag
    # Image paths
    startImgPath = "game/images/start_btn.png"
    instructionImgPath = "game/images/instructions_btn.png"
    exitImgPath = "game/images/exit_btn.png"

    # Create btnSprite class
    class btnSprite(pygame.sprite.Sprite):
        def __init__(self, img):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(os.path.join(img))
            self.rect = self.image.get_rect()
    
    # Create buttons using btnSprite class
    startImg = btnSprite(startImgPath)
    instructionImg = btnSprite(instructionImgPath)
    exitImg = btnSprite(exitImgPath)

    # Calculate the x value needed to place button in middle of screen
    centerX = (SCREEN_WIDTH / 2) - (startImg.image.get_width() / 2)
    
    # Set rect x and y values
    startImg.rect.x = centerX
    instructionImg.rect.x = centerX
    exitImg.rect.x = centerX
    startImg.rect.y = 100
    instructionImg.rect.y = 300
    exitImg.rect.y = 500

    # Add buttons to screen
    screen.blit(startImg.image, [startImg.rect.x, startImg.rect.y])
    screen.blit(instructionImg.image, [instructionImg.rect.x, instructionImg.rect.y])
    screen.blit(exitImg.image, [exitImg.rect.x, exitImg.rect.y])

    # If mousePos variable doesn't equal 0, check for collisions
    if mousePos != 0:
        if startImg.rect.collidepoint(mousePos):
            gameState = "setup"
        elif instructionImg.rect.collidepoint(mousePos):
            gameState = "instructions"
        elif exitImg.rect.collidepoint(mousePos):
            gameState = "exit"

    # Update screen
    pygame.display.update()


def instructionScreen():
    pygame.quit()
    sys.exit()


def drawGrid():
    global screen, gameState
    rect_size = 150
    circle_size = 60
    rect_x = (SCREEN_WIDTH / 2) - ((rect_size * 3) / 2)
    rect_y = (SCREEN_HEIGHT / 2) - ((rect_size * 3) / 2)

    screen.fill("white")
            
    for i in range(3):
         
        for j in range(3):
            # Creates a Rect object
            rect = pygame.Rect(rect_x, rect_y, rect_size, rect_size)
            # Draws the rect object on the screen
            pygame.draw.rect(screen, (0,0,0), rect, 2)
            # Draws a circle in the center of rect, but the circle is the came colour as the background
            circle = pygame.draw.circle(screen, ("white"), rect.center, circle_size)
            # Adds rect to cells list
            cells.append(rect)
            # Adds circle to circles list
            circles.append(circle)

            # Increments x value by size variable
            rect_x = (rect_x + rect_size)
        
        #Resets x value
        rect_x = rect_x - (rect_size * 3)
        # Increments y value by size variable
        rect_y = rect_y + rect_size

    gameState = "game"

    # Updates display
    pygame.display.update()


def gameLogic(mousePos):
    global screen, timer, gameState, cells, circles, score, timerText
    scoreText = font.render("Score: " + str(score), False, (0,0,0))

    class gameSprite(pygame.sprite.Sprite):
        def __init__(self, img):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(os.path.join(img))
            self.rect = self.image.get_rect()

    emptyCellPath = "game/images/emptyCell.png"
    plusDuckPath = "game/images/plusDuck.png"
    minusDuckPath = "game/images/minusDuck.png"

    emptyCell = gameSprite(emptyCellPath)
    plusDuck = gameSprite(plusDuckPath)
    minusDuck = gameSprite(minusDuckPath)

    # Timer label Code
    textRect = pygame.Rect(625, 20, 150, 30)
    textScreen = screen.subsurface(textRect)
    textScreen.fill("white")
    textScreen.blit(timerText, [0, 0])

    # Score label code
    scoreRect = pygame.Rect(625, 70, 150, 30)
    scoreScreen = screen.subsurface(scoreRect)
    scoreScreen.fill("white")
    scoreScreen.blit(scoreText, [0, 0])

    # Add empty cell images into cells
    for i in circles:
        screen.blit(emptyCell.image, [i.x, i.y])

    #timerRunning = True
    
    if timer > 0:
        cell1 = random.randint(0,8)
        cell2 = random.randint(0,8)

        plusDuck.rect.x = circles[cell1].x
        plusDuck.rect.y =  circles[cell1].y
        minusDuck.rect.x = circles[cell2].x
        minusDuck.rect.y = circles[cell2].y
            
        screen.blit(plusDuck.image, [plusDuck.rect.x, plusDuck.rect.y])
        screen.blit(minusDuck.image, [minusDuck.rect.x, minusDuck.rect.y])
        pygame.time.delay(100)

    if mousePos != 0:
        if plusDuck.rect.collidepoint(mousePos):
            score += 1
            scoreText = font.render("Score: " + str(score), False, (0,0,0))
            mousePos = 0
            #print("Yes")
        elif minusDuck.rect.collidepoint(mousePos):
            score -= 1
            scoreText = font.render("Score: " + str(score), False, (0,0,0))
            mousePos = 0
            #print("No")

    print(mousePos)
        
    pygame.display.update()
    


    
# Always be at bottom of file
asyncio.run(main())

