# settings.py

# Dimensões da tela
WIDTH = 800
HEIGHT = 600

# Taxa de atualização
FPS = 60

# Cores (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Configurações do Jogador
PLAYER_SPEED = 10
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 20

# Configurações do Asteroide
ASTEROID_SPEED = 3
ASTEROID_SIZE = 30
SPAWN_RATE = 60 # Cria um asteroide a cada N frames (a 60 FPS, 1 por segundo)

# Configurações do Projétil
BULLET_SPEED = -7 # Negativo pois sobe na tela (o y diminui)
BULLET_WIDTH = 4
BULLET_HEIGHT = 15
