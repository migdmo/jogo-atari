# player.py
import pygame
from settings import WIDTH, HEIGHT, GREEN, PLAYER_SPEED, PLAYER_WIDTH, PLAYER_HEIGHT

class Player:
    def __init__(self):
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        # Centralizado horizontalmente, perto da base
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 10
        self.speed = PLAYER_SPEED
        self.color = GREEN
        
        # O Rect facilita desenho e detecção de colisões no pygame
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys):
        # Mover para a esquerda se não encostar na borda esquerda
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        # Mover para a direita se não encostar na borda direita
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
