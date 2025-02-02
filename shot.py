import pygame

import circleshape
from constants import SHOT_RADIUS


class Shot(circleshape.CircleShape):
    def __init__(self, x, y,):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt