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
    player = Player(SCREEN_HEIGHT / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # pygame.Surface.fill(screen, color=(0,0,0))
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        player.update(dt)

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()