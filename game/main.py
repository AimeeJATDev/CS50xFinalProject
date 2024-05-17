# Game Colour Palette: https://colorhunt.co/palette/11009e4942e4e6b9defae7f3

# Import Libraries
import os
import sys
import pygame
import asyncio
import random

#PyGame Initialisation
pygame.init()
pygame.font.init()

# Variable Declaration
SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
caption = pygame.display.set_caption("Whack-a-Duck")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Calibri", 30)
running = True
gameState = "start"
cells = []
circles = []
score = 0
cell1 = random.randint(0,8)
cell2 = random.randint(0,8)
startTime = pygame.time.get_ticks()
scoreText = font.render("Score: " + str(score), False, (0,0,0))

# Timer Set Up
timer = 20
timerInterval = 1000
timerEvent = pygame.USEREVENT + 1
pygame.time.set_timer(timerEvent, timerInterval)
timerText = font.render("Time: " + str(timer), False, [0,0,0])

# Creation of gameSprite class
class gameSprite(pygame.sprite.Sprite):
        def __init__(self, img, clicked):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(os.path.join(img))
            self.rect = self.image.get_rect()
            self.clicked = clicked

# TODO: Remove game/ from path before packaging with pygbag
# Image paths
startImgPath = "game/images/start_btn.png"
instructionImgPath = "game/images/instructions_btn.png"
exitImgPath = "game/images/exit_btn.png"

emptyCellPath = "game/images/emptyCell.png"
plusDuckPath = "game/images/plusDuck.png"
minusDuckPath = "game/images/minusDuck.png"

# Creation of sprites using the gameSprite class
startImg = gameSprite(startImgPath, False)
instructionImg = gameSprite(instructionImgPath, False)
exitImg = gameSprite(exitImgPath, False)

emptyCell = gameSprite(emptyCellPath, False)
plusDuck = gameSprite(plusDuckPath, False)
minusDuck = gameSprite(minusDuckPath, False)


# Main Function
async def main():
    global screen, clock, timer, running, timerText, score, scoreText, gameState
    
    # Main loop for the game
    while running:
        for event in pygame.event.get():
            # If the game is quit, stop the main loop
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if gameState == "start":
                    if startImg.rect.collidepoint(event.pos):
                        gameState = "setup"
                    elif instructionImg.rect.collidepoint(event.pos):
                        gameState = "instructions"
                    elif exitImg.rect.collidepoint(event.pos):
                        gameState = "exit"
                elif gameState == "game":
                    if plusDuck.rect.collidepoint(event.pos):
                        if plusDuck.clicked == False:
                            score += 1
                            plusDuck.clicked = True
                            scoreText = font.render("Score: " + str(score), False, (0,0,0))
                    elif minusDuck.rect.collidepoint(event.pos):
                        if minusDuck.clicked == False:
                            score -= 1
                            minusDuck.clicked = True
                            scoreText = font.render("Score: " + str(score), False, (0,0,0))
            elif event.type == timerEvent:
                timer -= 1
                timerText = font.render("Time: " + str(timer), False, [0,0,0])
                if timer == 0:
                    pygame.time.set_timer(timerEvent, 0)

        if gameState == "start":
            titleScreen()
        elif gameState == "instructions":
            instructionScreen()
        elif gameState == "setup":
            drawGrid()
        elif gameState == "game":
            gameLogic()
        elif gameState == "endgame":
            endScreen()
        elif gameState == "exit":
            pygame.quit()
            sys.exit()
    
        pygame.display.flip()
        clock.tick(30)

        await asyncio.sleep(0)

    pygame.quit()


def titleScreen():
    global screen, gameState

    # Fills screen with colour
    screen.fill("#11009E")

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


def gameLogic():
    global screen, timer, gameState, circles, score, timerText, cell1, cell2, startTime, scoreText

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
    
    if timer > 0:
        if pygame.time.get_ticks() - startTime > 500:
            cell1 = random.randint(0,8)
            cell2 = random.randint(0,8)
            plusDuck.clicked = False
            minusDuck.clicked = False
            if cell1 == cell2:
                cell1 = random.randint(0,8)
                cell2 = random.randint(0,8)
            else:
                startTime = pygame.time.get_ticks()
                plusDuck.rect.x = circles[cell1].x
                plusDuck.rect.y =  circles[cell1].y
                minusDuck.rect.x = circles[cell2].x
                minusDuck.rect.y = circles[cell2].y
        screen.blit(plusDuck.image, [plusDuck.rect.x, plusDuck.rect.y])
        screen.blit(minusDuck.image, [minusDuck.rect.x, minusDuck.rect.y])
    elif timer <= 0:
        gameState = "endgame"


def endScreen():
    global screen, score

    screen.fill("white")

    if score > 0:
        successText = font.render("Congratulations!", False, (0,0,0))
        screen.blit(successText, [0,0])
    elif score <= 0:
        failText = font.render("Game Over!", False, (0,0,0))
        screen.blit(failText, [0,0])

    finalScoreText = font.render("Your Score: " + str(score), False, (0,0,0))
    screen.blit(finalScoreText, [0,40])
        
        
    pygame.display.update()
    

# Always be at bottom of file
asyncio.run(main())

