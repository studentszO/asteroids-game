import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20.0, 50.0)
            new_asteroid_vector = self.velocity.rotate(random_angle)
            new_asteroid_vector_two = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            second_new_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid.velocity = new_asteroid_vector_two * 1.2
            second_new_asteroid.velocity = new_asteroid_vector * 1.2

    