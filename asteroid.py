import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, LINE_WIDTH )


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        old_radius = self.radius


        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        r = random.uniform(20,50)
        first_asteroid_new_vector = self.velocity.rotate(r)
        second_asteroid_new_vector = self.velocity.rotate(-r)

        new_radius = old_radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        first_asteroid.velocity = first_asteroid_new_vector * 1.2
        second_asteroid.velocity = second_asteroid_new_vector * 1.2

