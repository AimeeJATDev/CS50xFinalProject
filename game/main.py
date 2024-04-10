import pygame
import asyncio

#PyGame initialisation
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

async def main():
    global screen, clock, running
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("Blue")

        # GAME CODE HERE

        pygame.display.flip()
        clock.tick(60)

        await asyncio.sleep(0)

    pygame.quit()
asyncio.run(main())
