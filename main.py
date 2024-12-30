import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock ()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    allasteroids = pygame.sprite.Group()
    Asteroid.containers = (allasteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    allshots = pygame.sprite.Group()
    Shot.containers = (allshots, updatable, drawable)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updating in updatable:
            updating.update(dt)
        for asteroid in allasteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()
        for asteroid in allasteroids:
            for shot in allshots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
        screen.fill((0,0,0))
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__=="__main__":
    main()

