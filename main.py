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

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_HEIGHT / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, color=(0,0,0))
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        print(dt)


if __name__ == "__main__":
    main()