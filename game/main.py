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
    size = 100

    class Cell:
        def __init__(self, x, y):
            self.x = x
            self.y = y
 
    rect = pygame.Rect(450, 150, 400, 400)
    pygame.draw.rect(screen, (0,0,0), rect, 2)


    for i in range(1, 4):
        cells = []
        rect_y = i * size

        for j in range(1, 4):
            
            rect_x = j * size
            rect = pygame.Rect(rect_x, rect_y, size, size)
            pygame.draw.rect(screen, (0,0,0), rect, 2)
            cell = Cell(rect_x, rect_y)
            cells.append(cell)

    
    for i in range(len(cells)):
        print(cells[i].x, cells[i].y)
        
        
            
    
    # First iteration of grid

    #rect_1 = pygame.Rect(0, 0, 100, 100)
    #rect_2 = pygame.Rect(100, 0 , 100, 100)
    #rect_3 = pygame.Rect(200, 0, 100, 100)

    #rect_4 = pygame.Rect(0, 100, 100, 100)
    #rect_5 = pygame.Rect(100, 100 , 100, 100)
    #rect_6 = pygame.Rect(200, 100, 100, 100)

    #rect_7 = pygame.Rect(0, 200, 100, 100)
    #rect_8 = pygame.Rect(100, 200 , 100, 100)
    #rect_9 = pygame.Rect(200, 200, 100, 100)

    
    #pygame.draw.rect(screen, (0,0,0), rect_1, 2)
    #pygame.draw.rect(screen, (0,0,0), rect_2, 2)
    #pygame.draw.rect(screen, (0,0,0), rect_3, 2)

    #pygame.draw.rect(screen, (0,0,0), rect_4, 2)
    #pygame.draw.rect(screen, (0,0,0), rect_5, 2)

    #pygame.draw.rect(screen, (0,0,0), rect_6, 2)

    #pygame.draw.rect(screen, (0,0,0), rect_7, 2)
    #pygame.draw.rect(screen, (0,0,0), rect_8, 2)
    #pygame.draw.rect(screen, (0,0,0), rect_9, 2)

    pygame.display.update()

# Always be at bottom of file
asyncio.run(main())

