import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shooting import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT }")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updatable:
            thing.update(dt)

        for item in asteroids:
            if item.collision(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if item.collision(bullet):
                    item.split()
                    bullet.kill()

        pygame.Surface.fill(screen, (0,0,0))

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()
