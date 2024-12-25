import pygame
from constants import (SCREEN_HEIGHT,
                        SCREEN_WIDTH,
                        ASTEROID_KINDS, 
                        ASTEROID_MAX_RADIUS, 
                        ASTEROID_MIN_RADIUS, 
                        ASTEROID_SPAWN_RATE,
                        PLAYER_RADIUS)
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)

    player = Player(SCREEN_HEIGHT / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        for object in drawable_group:
            object.draw(screen)
        pygame.display.flip()
        for object in updatable_group:
            object.update(dt)

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()