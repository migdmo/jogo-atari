# main.py
import pygame
import sys
from settings import *
from player import Player
from asteroid import Asteroid
from bullet import Bullet

def main():
    # Inicializa todos os módulos importados do pygame
    pygame.init()
    
    # Configura a janela
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jogo Atari")
    clock = pygame.time.Clock()
    
    # Fonte para desenhar a pontuação
    font = pygame.font.SysFont(None, 36)
    
    # Instancia entidades do jogo
    player = Player()
    asteroids = []
    bullets = []
    
    score = 0
    frame_count = 0
    running = True
    game_over = False
    
    # Loop Principal do Jogo
    while running:
        clock.tick(FPS) # Garante que o jogo vai rodar em FPS constante
        frame_count += 1
        
        # 1. Processamento de Eventos (input do usuário)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN and not game_over:
                # Disparo na barra de espaço
                if event.key == pygame.K_SPACE:
                    # Instancia o projétil no meio superior do retângulo do jogador
                    b = Bullet(player.rect.centerx, player.rect.top)
                    bullets.append(b)
        
        # 2. Atualizações e Lógica do Jogo
        if not game_over:
            # Captura as teclas sendo pressionadas para o movimento suave
            keys = pygame.key.get_pressed()
            player.move(keys)
            
            # Controla o spawn de novos asteroides
            if frame_count % SPAWN_RATE == 0:
                asteroids.append(Asteroid())
                
            # Atualiza os tiros
            for b in bullets[:]:
                b.update()
                if b.off_screen:
                    bullets.remove(b)
                    
            # Atualiza os asteroides
            for a in asteroids[:]:
                a.update()
                
                # Condição de Derrota 1: Bater na nave
                if a.rect.colliderect(player.rect):
                    game_over = True
                    break
                    
                # Condição de Derrota 2: Chegar no fundo da tela
                if a.rect.bottom >= HEIGHT:
                    game_over = True
                    break
                    
                if a.off_screen:
                    asteroids.remove(a)
                    
            # Verifica colisão entre os tiros e os asteroides
            for b in bullets[:]:
                hit = False
                for a in asteroids[:]:
                    if b.rect.colliderect(a.rect):
                        asteroids.remove(a)
                        hit = True
                        score += 10 # Aumenta a pontuação
                        break
                # Se o tiro acertou algo, ele também desaparece
                if hit:
                    bullets.remove(b)
        
        # 3. Renderização (Desenho na tela)
        screen.fill(BLACK) # Limpa a tela com fundo preto
        
        # Desenha as entidades se o jogo não acabou
        player.draw(screen)
        for a in asteroids:
            a.draw(screen)
        for b in bullets:
            b.draw(screen)
            
        # Desenha a pontuação
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        # Desenha mensagem de Game Over
        if game_over:
            game_over_text = font.render("GAME OVER", True, RED)
            # Centraliza a mensagem
            x_pos = WIDTH // 2 - game_over_text.get_width() // 2
            y_pos = HEIGHT // 2 - game_over_text.get_height() // 2
            screen.blit(game_over_text, (x_pos, y_pos))
        
        # Atualiza a janela inteira com as novidades
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
