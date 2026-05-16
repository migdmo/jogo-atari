# bullet.py
import pygame
from settings import WHITE, BULLET_SPEED, BULLET_WIDTH, BULLET_HEIGHT

class Bullet:
    def __init__(self, x, y):
        self.width = BULLET_WIDTH
        self.height = BULLET_HEIGHT
        # Centraliza o tiro em relação ao ponto passado
        self.rect = pygame.Rect(x - self.width // 2, y, self.width, self.height)
        self.speed = BULLET_SPEED
        self.color = WHITE
        self.off_screen = False

    def update(self):
        self.rect.y += self.speed
        # Se passar do limite superior, marcamos como fora da tela
        if self.rect.bottom < 0:
            self.off_screen = True

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
