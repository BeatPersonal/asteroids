import pygame
from pygame import display
from pygame.examples.sprite_texture import clock

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock
    dt = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            screen.fill("black")
            display.flip()

            # limite the framerate to 60 FPS
            dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
