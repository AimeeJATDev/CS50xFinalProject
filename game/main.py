import pygame
import asyncio

#PyGame initialisation
pygame.init()
SCREEN_WIDTH = 1280
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
        drawGrid()

        pygame.display.flip()
        clock.tick(60)

        await asyncio.sleep(0)

    pygame.quit()


def drawGrid():
    global screen
    rect_x = 450
    rect_y = 150
    size = 150

    class Cell:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    for i in range(3):
        cells = []
    
        for j in range(3):
            # Creates a Rect object
            rect = pygame.Rect(rect_x, rect_y, size, size)
            # Draws the rect object on the screen
            pygame.draw.rect(screen, (0,0,0), rect, 2)

            # Creates a Cell object
            cell = Cell(rect_x, rect_y)
            # Adds cell to cells list
            cells.append(cell)

            # Increments x value by size variable
            rect_x = (rect_x + size)
        
        #Resets x value
        rect_x = rect_x - (size * 3)
        # Increments y value by size variable
        rect_y = rect_y + size

    # Updates display
    pygame.display.update()

# Always be at bottom of file
asyncio.run(main())

