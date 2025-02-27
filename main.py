import pygame
import sys
from constants import (SCREEN_HEIGHT,
                        SCREEN_WIDTH,
                        ASTEROID_KINDS, 
                        ASTEROID_MAX_RADIUS, 
                        ASTEROID_MIN_RADIUS, 
                        ASTEROID_SPAWN_RATE,
                        PLAYER_RADIUS,
                        PLAYER_SHOOT_COOLDOWN)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    shots_group = pygame.sprite.Group()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shots_group, drawable_group, updatable_group)

    player = Player(SCREEN_HEIGHT / 2, SCREEN_HEIGHT / 2)
    asteroids_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('#D30DA3')
            
        for object in drawable_group:
            object.draw(screen)

        pygame.display.flip()

        for object in updatable_group:
            object.update(dt)
        
        for asteroid in asteroids_group:
            if asteroid.check_collision(player):
                print("GAME OVER!")
                sys.exit()
            for shot in shots_group:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()