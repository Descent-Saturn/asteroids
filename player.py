import pygame
from constants import PLAYER_RADIUS,PLAYER_TURN_SPEED,PLAYER_SPEED,PLAYER_SHOOT_SPEED,PLAYER_SHOOT_COOLDOWN
from circle_shape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw (self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
    def rotate (self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if self.timer > 0:
            self.timer -= dt
    def move (self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def shoot (self):
        if self.timer <= 0:
            bullet_direction = pygame.Vector2(0,1).rotate(self.rotation)
            bullet_velocity = bullet_direction * PLAYER_SHOOT_SPEED
            Shot(self.position.x, self.position.y, bullet_velocity)
            self.timer = PLAYER_SHOOT_COOLDOWN
