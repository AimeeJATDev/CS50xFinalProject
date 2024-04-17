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

async def main():
    global screen, clock, running
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("White")

        # GAME CODE HERE

        titleScreen()

        pygame.display.flip()
        clock.tick(60)

        await asyncio.sleep(0)

    pygame.quit()

def titleScreen():
    global screen

    startImgPath = "game/images/test.jpg"
    instructionImgPath = "game/images/..."
    exitImgPath = "game/images/..."
    
    startImg = pygame.image.load(os.path.join(startImgPath))
    instructionImg = pygame.image.load(os.path.join(instructionImgPath))
    exitImg= pygame.image.load(os.path.join(exitImgPath))

    screen.blit(startImg, (0,0))
    screen.blit(instructionImg, (0,0))
    screen.blit(exitImg, (0,0))

    
    #drawGrid()


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

