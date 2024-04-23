# Game Colour Palette: https://colorhunt.co/palette/11009e4942e4e6b9defae7f3

import os
import pygame
import asyncio

#PyGame initialisation
pygame.init()
SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Whack-a-Duck")
clock = pygame.time.Clock()
running = True
gameState = "start_menu"

async def main():
    global screen, clock, running
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print("click")


        # GAME CODE HERE

        if gameState == "start_menu":
            titleScreen()
        elif gameState == "game":
            print("game")
    
        pygame.display.flip()
        clock.tick(60)

        await asyncio.sleep(0)

    pygame.quit()

#def mouse():
    #pos = pygame.mouse.get_pos()
    #for event in pygame.event.get():
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #pos = pygame.mouse.get_pos()
    #return pos

def titleScreen():
    global screen, gameState

    screen.fill("#11009E")

    # TODO: Remove game/ from path before packaging with pygbag
    startImgPath = "game/images/start_btn.png"
    instructionImgPath = "game/images/instructions_btn.png"
    exitImgPath = "game/images/exit_btn.png"

    class btnSprite(pygame.sprite.Sprite):
        def __init__(self, img):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(os.path.join(img))
            self.rect = self.image.get_rect()
    
    startImg = btnSprite(startImgPath)
    instructionImg = btnSprite(instructionImgPath)
    exitImg = btnSprite(exitImgPath)

    centerX = (SCREEN_WIDTH / 2) - (startImg.image.get_width() / 2)
    centerY = (SCREEN_HEIGHT / 2) - (startImg.image.get_height() / 2)

    screen.blit(startImg.image, [centerX, 100])
    screen.blit(instructionImg.image, [centerX, 300])
    screen.blit(exitImg.image, [centerX, 500])

    # TODO: https://www.geeksforgeeks.org/mmouse-clicks-on-sprites-in-pygame/

    #if startImg.rect.collidepoint():
        #drawGrid()
    #elif instructionImg.rect.collidepoint():
        #print("Instructions")
    #elif exitImg.rect.collidepoint():
        #pygame.quit()

    gameState = "game"    
    pygame.display.flip()


def drawGrid():
    global screen
    rect_x = 400
    rect_y = 150
    rect_size = 150
    circle_size = 60

    class Cell:
        def __init__(self, x, y, center):
            self.x = x
            self.y = y
            self.center = center

    for i in range(3):
        cells = []
    
        for j in range(3):
            # Creates a Rect object
            rect = pygame.Rect(rect_x, rect_y, rect_size, rect_size)
            # Draws the rect object on the screen
            pygame.draw.rect(screen, (0,0,0), rect, 2)
            # Draws a circle in the center of rect
            pygame.draw.circle(screen, (0,0,0), rect.center, circle_size)

            # Creates a Cell object and saves coordinates of x, y and center
            cell = Cell(rect_x, rect_y, rect.center)
            # Adds cell to cells list
            cells.append(cell)

            # Increments x value by size variable
            rect_x = (rect_x + rect_size)
        
        #Resets x value
        rect_x = rect_x - (rect_size * 3)
        # Increments y value by size variable
        rect_y = rect_y + rect_size
    
    for i in range(len(cells)):
        print(cells[i].x, cells[i].y)

    # Updates display
    pygame.display.update()

# Always be at bottom of file
asyncio.run(main())

