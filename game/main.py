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

    # Updates display
    pygame.display.update()

# Always be at bottom of file
asyncio.run(main())

