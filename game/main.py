# Game Colour Palette: https://colorhunt.co/palette/1b262c0f4c753282b8bbe1fa

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
aldrichFont = pygame.font.Font("game/fonts/aldrich/Aldrich-Regular.ttf", 30)
running = True
gameState = "start"
cells = []
circles = []
score = 0
cell1 = random.randint(0,8)
cell2 = random.randint(0,8)
startTime = pygame.time.get_ticks()
scoreText = aldrichFont.render("Score: " + str(score), False, (0,0,0))
username = ""

# Timer Set Up
timer = 20
timerInterval = 1000
timerEvent = pygame.USEREVENT + 1
pygame.time.set_timer(timerEvent, timerInterval)
timerText = aldrichFont.render("Time: " + str(timer), False, [0,0,0])

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
titleScreenImgPath = "game/images/title_screen_btn.png"

instructionScreenImgPath = "game/images/instructions.png"

gridBackgroundPath = "game/images/gridBackground.png"
lblBackgroundPath = "game/images/lblBackground.png"
emptyCellPath = "game/images/emptyCell.png"
plusDuckPath = "game/images/plusDuck.png"
minusFishPath = "game/images/minusFish.png"

endScreenBackgroundPath = "game/images/endScreenBackground.png"
nextImgPath = "game/images/next_btn.png"

# Creation of sprites using the gameSprite class

startImg = gameSprite(startImgPath, False)
instructionImg = gameSprite(instructionImgPath, False)
exitImg = gameSprite(exitImgPath, False)
titleScreenImg = gameSprite(titleScreenImgPath, False)

instructionScreenImg = gameSprite(instructionScreenImgPath, False)

gridBackground = gameSprite(gridBackgroundPath, False)
lblBackground = gameSprite(lblBackgroundPath, False)
emptyCell = gameSprite(emptyCellPath, False)
plusDuck = gameSprite(plusDuckPath, False)
minusFish = gameSprite(minusFishPath, False)

endScreenBackground = gameSprite(endScreenBackgroundPath, False)
nextImg = gameSprite(nextImgPath, False)


# Main Function
async def main():
    global screen, clock, timer, running, timerText, score, scoreText, gameState, username
    
    # Main loop for the game
    while running:
        for event in pygame.event.get():
            # If the game is quit, stop the main loop
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If gameState is start, check for collisions on each of the title screen buttons
                if gameState == "start":
                    if startImg.rect.collidepoint(event.pos):
                        gameState = "setup"
                    elif instructionImg.rect.collidepoint(event.pos):
                        gameState = "instructions"
                    elif exitImg.rect.collidepoint(event.pos):
                        gameState = "exit"
                elif gameState == "instructions":
                    if titleScreenImg.rect.collidepoint(event.pos):
                        gameState = "start"
                elif gameState == "scoreInput":
                    if exitImg.rect.collidepoint(event.pos):
                        gameState = "exit"
                # Else if gameState is game, check for collisions for each of the moving sprites in the game
                elif gameState == "game":
                    if plusDuck.rect.collidepoint(event.pos):
                        if plusDuck.clicked == False:
                            score += 1
                            plusDuck.clicked = True
                            scoreText = aldrichFont.render("Score: " + str(score), False, (0,0,0))
                    elif minusFish.rect.collidepoint(event.pos):
                        if minusFish.clicked == False:
                            score -= 1
                            minusFish.clicked = True
                            scoreText = aldrichFont.render("Score: " + str(score), False, (0,0,0))
                elif gameState == "endgame":
                    if nextImg.rect.collidepoint(event.pos):
                        gameState = "scoreInput"
            elif event.type == pygame.KEYDOWN and gameState == "scoreInput":
                if event.key == pygame.K_RETURN:
                    print(username)
                elif event.key == pygame.K_BACKSPACE:
                    username = username + "\b"
                else:
                    username += event.unicode
            elif event.type == timerEvent and gameState == "game":
                timer -= 1
                timerText = aldrichFont.render("Time: " + str(timer), False, [0,0,0])
                if timer == 0:
                    pygame.time.set_timer(timerEvent, 0)

        # If/Else statement to call the different functions depending on what the gameState is
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
        elif gameState == "scoreInput":
            scoreInput()
        elif gameState == "exit":
            pygame.quit()
            sys.exit()
    
        # Updates screen
        pygame.display.flip()
        clock.tick(30)

        await asyncio.sleep(0)

    pygame.quit()


def titleScreen():
    # Declare global variables to be used in this function
    global screen, gameState
    # Fills screen with colour
    screen.fill("#1B262C")

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
    global screen

    # Calculates the x value for the button
    titleImgX = (SCREEN_WIDTH / 2) - (titleScreenImg.rect.width / 2)
    instructionImgX = (SCREEN_WIDTH / 2) - (instructionScreenImg.rect.width / 2)
    
    # Fills the screen background
    screen.fill("#1B262C")

    # Initialises the x and y values for the button
    titleScreenImg.rect.x = titleImgX
    titleScreenImg.rect.y = 600
    instructionScreenImg.rect.x = instructionImgX
    instructionScreenImg.rect.y = 150

    # Adds the button to the screen
    screen.blit(instructionScreenImg.image, [instructionScreenImg.rect.x, instructionScreenImg.rect.y])
    screen.blit(titleScreenImg.image, [titleScreenImg.rect.x, titleScreenImg.rect.y])


def drawGrid():
    # Declare global variables to be used in this function
    global screen, gameState

    # Declare local variables
    rect_size = 150
    circle_size = 60
    # Calculate where the x and y values of the grid so it can be centered on the screen
    rect_x = (SCREEN_WIDTH / 2) - ((rect_size * 3) / 2)
    rect_y = (SCREEN_HEIGHT / 2) - ((rect_size * 3) / 2)

    gridBackground.rect.x = rect_x
    gridBackground.rect.y = rect_y

    # Fill the screen with a white colour
    screen.fill("#3282B8")

    screen.blit(gridBackground.image, [gridBackground.rect.x, gridBackground.rect.y])
            
    for i in range(3):
        for j in range(3):
            # Creates a Rect object
            rect = pygame.Rect(rect_x, rect_y, rect_size, rect_size)
            # Draws the rect object on the screen
            pygame.draw.rect(screen, (0,0,0), rect, 2)
            # Draws a circle in the center of rect, but the circle is the came colour as the background
            circle = pygame.draw.circle(screen, ("#1B262C"), rect.center, circle_size)
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

    # Changes gameState variable to "game"
    gameState = "game"

    # Updates display
    pygame.display.update()


def gameLogic():
    global screen, timer, gameState, circles, score, timerText, cell1, cell2, startTime, scoreText

    # Add background image to screen
    screen.blit(lblBackground.image, [625, 20])

    # Add timer and score labels to screen
    screen.blit(timerText, [655, 35])
    screen.blit(scoreText, [655, 75])
    
    # Add empty cell images into cells
    for i in circles:
        screen.blit(emptyCell.image, [i.x, i.y])
    
    if timer > 0:
        # Change the position of the sprites every 500ms
        if pygame.time.get_ticks() - startTime > 500:
            cell1 = random.randint(0,8)
            cell2 = random.randint(0,8)
            plusDuck.clicked = False
            minusFish.clicked = False
            # If both cell1 and cell2 are equal get another random value for cell2
            if cell1 == cell2:
                #cell1 = random.randint(0,8)
                cell2 = random.randint(0,8)
            # If both cell1 and cell two show a different value change the x and y values of the sprites and reset the startTime variable
            else:
                startTime = pygame.time.get_ticks()
                plusDuck.rect.x = circles[cell1].x
                plusDuck.rect.y =  circles[cell1].y
                minusFish.rect.x = circles[cell2].x
                minusFish.rect.y = circles[cell2].y
        # Update the sprites position on screen
        screen.blit(plusDuck.image, [plusDuck.rect.x, plusDuck.rect.y])
        screen.blit(minusFish.image, [minusFish.rect.x, minusFish.rect.y])
    # If the timer has run out change the gameState to "endgame"
    elif timer <= 0:
        gameState = "endgame"


def endScreen():
    global screen, score

    # Initalise Rect - to be used for subsurface
    finalScreenRect = pygame.Rect(0,0, 300, 100)

    # Calculates the x values of each component to ensure they are in the center of the screen
    finalScreenX = (SCREEN_WIDTH / 2) - (finalScreenRect.width/ 2)
    nextImageX = (SCREEN_WIDTH / 2) - (nextImg.rect.width / 2)
    bgImageX = (SCREEN_WIDTH / 2) - (endScreenBackground.rect.width / 2)

    # Assign x and y values
    finalScreenRect.x = finalScreenX
    finalScreenRect.y = 260
    nextImg.rect.x = nextImageX
    nextImg.rect.y = 600
    endScreenBackground.rect.x = bgImageX
    endScreenBackground.rect.y = 150

    # Creates subsurface
    finalScreen = screen.subsurface(finalScreenRect)

    screen.fill("#1B262C")
    screen.blit(endScreenBackground.image, [endScreenBackground.rect.x, endScreenBackground.rect.y])

    if score > 0:
        successText = aldrichFont.render("Congratulations!", False, (0,0,0))
        centerTextX = (finalScreenRect.width / 2) - (successText.get_width() / 2)
        finalScreen.blit(successText, [centerTextX, 10])
    elif score <= 0:
        failText = aldrichFont.render("Game Over!", False, (0,0,0))
        centerTextX = (finalScreenRect.width / 2) - (failText.get_width() / 2)
        finalScreen.blit(failText, [centerTextX, 10])

    finalScoreText = aldrichFont.render("Your Score: " + str(score), False, (0,0,0))
    centerTextX = (finalScreenRect.width / 2) - (finalScoreText.get_width() / 2)
    finalScreen.blit(finalScoreText, [centerTextX, 50])
    screen.blit(nextImg.image, [nextImg.rect.x, nextImg.rect.y])
        
    pygame.display.update()


def scoreInput():
    global screen, score

    screen.fill("#1B262C")

    usernameInputRect = pygame.Rect(0, 0, 200, 200)

    usernameText = aldrichFont.render("Please enter your name", False, (0,0,0))
    usernameInput = aldrichFont.render(username, False, (0,0,0))

    backgroundX = (SCREEN_WIDTH / 2) - (endScreenBackground.rect.width / 2)
    usernameTextX = (SCREEN_WIDTH / 2) - (usernameText.get_width() / 2)
    exitBtnX = (SCREEN_WIDTH / 2) - (exitImg.rect.width / 2)

    endScreenBackground.rect.x = backgroundX
    endScreenBackground.rect.y = 150
    exitImg.rect.x = exitBtnX
    exitImg.rect.y = 600

    screen.blit(endScreenBackground.image, [endScreenBackground.rect.x, endScreenBackground.rect.y])
    screen.blit(usernameText, [usernameTextX, 200])
    screen.blit(usernameInput, [0, 20])
    screen.blit(exitImg.image, [exitImg.rect.x, exitImg.rect.y])
    

# Always be at bottom of file
asyncio.run(main())

