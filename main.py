import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock_object = pygame.time.Clock()
    dt = 0

    running = True
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.quit:
                return 

        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock_object.tick(60)
        dt = clock_object.tick() / 1000.0

    pygame.quit()


if __name__ == "__main__":
    main()
