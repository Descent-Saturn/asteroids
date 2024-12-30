import pygame
from circle_shape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Initialize with CircleShape's constructor

    def draw(self, surface):
        # Access the `x` and `y` from the `position` vector
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # Update position using the velocity vector
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        vectorone = self.velocity.rotate(+angle)
        vectortwo = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        new_asteroid.velocity = vectorone * 1.2
        new_second_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        new_second_asteroid.velocity = vectortwo * 1.2
