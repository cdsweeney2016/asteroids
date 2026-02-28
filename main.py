import pygame
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SHOOT_COOLDOWN_SECONDS
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
import sys

def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock_object = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = updatable, drawable

    asteroids = pygame.sprite.Group()
    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = updatable

    shots = pygame.sprite.Group()
    Shot.containers = shots, updatable, drawable

    field_object = AsteroidField()
    player_object = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2, PLAYER_SHOOT_COOLDOWN_SECONDS=PLAYER_SHOOT_COOLDOWN_SECONDS)
    
    player_score = 0

    running = True

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        screen.fill((0, 0, 0))
        
        for thing in drawable:
            thing.draw(screen)

        #Asteroid Cheeeck
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    if asteroid.radius <= 20:
                        player_score += 10

        pygame.display.flip()

        dt = clock_object.tick(60) / 1000.0
        updatable.update(dt)

        for asteroid in asteroids:
            if player_object.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")

                print(f"Final Score: {player_score}")
                sys.exit()
        
    pygame.quit()


if __name__ == "__main__":
    main()
