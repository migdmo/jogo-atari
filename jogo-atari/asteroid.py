# asteroid.py
import pygame
import random
from settings import WIDTH, HEIGHT, WHITE, ASTEROID_SPEED, ASTEROID_SIZE

class Asteroid:
    def __init__(self):
        self.size = ASTEROID_SIZE
        # Aparece numa posição X aleatória
        self.x = random.randint(0, WIDTH - self.size)
        # Nasce um pouco acima da tela visível
        self.y = -self.size
        self.speed = ASTEROID_SPEED
        self.color = WHITE
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.off_screen = False

    def update(self):
        self.rect.y += self.speed
        # Se ultrapassar a tela por baixo, marcamos como fora da tela
        if self.rect.top > HEIGHT:
            self.off_screen = True

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
