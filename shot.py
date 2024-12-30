import pygame
from constants import SHOT_RADIUS,PLAYER_SHOOT_SPEED
from circle_shape import CircleShape

class Shot(CircleShape):
    containers = None
    def __init__(self,x,y,velocity):
        super().__init__(x,y,SHOT_RADIUS)
        self.velocity = velocity
        self.color = (255,255,255)
        self.add(self.containers)
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)
    def update(self, dt):
        # Update position based on velocity and time
        self.position += self.velocity * dt
