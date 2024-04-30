# Game Colour Palette: https://colorhunt.co/palette/11009e4942e4e6b9defae7f3

import os
import sys
import pygame
import asyncio

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
gameState = "start_menu"
mousePos = 0
cells = []
circles = []
score = 0

timer = 10
timerInterval = 1000
timerEvent = pygame.USEREVENT + 1
pygame.time.set_timer(timerEvent, timerInterval)

async def main():
    global screen, clock, timer, running, mousePos
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
            elif event.type == timerEvent:
                timer -= 1
                #text = font.render("Time: " + str(time), False, [0,0,0])
                if timer == 0:
                    pygame.time.set_timer(timerEvent, 0)

        if gameState == "start_menu":
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
        clock.tick(60)

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
    global screen, gameState, font, score
    rect_size = 150
    circle_size = 60
    rect_x = (SCREEN_WIDTH / 2) - ((rect_size * 3) / 2)
    rect_y = (SCREEN_HEIGHT / 2) - ((rect_size * 3) / 2)
    scoreText = font.render("Score: " + str(score), False, (0,0,0))

    screen.fill("white")
            
    for i in range(3):
         
        for j in range(3):
            # Creates a Rect object
            rect = pygame.Rect(rect_x, rect_y, rect_size, rect_size)
            # Draws the rect object on the screen
            pygame.draw.rect(screen, (0,0,0), rect, 2)
            # Draws a circle in the center of rect
            circle = pygame.draw.circle(screen, (0,0,0), rect.center, circle_size)
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

    screen.blit(scoreText, [rect_x, 50])

    gameState = "game"

    # Updates display
    pygame.display.update()


def gameLogic(mousePos):
    global screen, clock, timer, gameState, cells, circles, score

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

    text = font.render("Time: " + str(timer), False, [0,0,0])
    screen.blit(text, [0,0])

    pygame.display.update()
    


    
# Always be at bottom of file
asyncio.run(main())

