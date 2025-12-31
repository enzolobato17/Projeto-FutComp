import os
import pygame
import sys
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pygame.init()
pygame.mixer.init()

# #Músicas
# pygame.mixer.music.load(os.path.join(BASE_DIR, "bolarolando.mp3"))
# pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.play(-1)

# barulho_gol = pygame.mixer.Sound(os.path.join(BASE_DIR, "gol.mp3"))
# barulho_gol.set_volume(0.5)

#Janela
largura = 1280
altura = 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("FutCOMP")
clock = pygame.time.Clock()

#Textos
score_font = pygame.font.Font(None, 100)
gol_font = pygame.font.Font(None, 140)
texto_gol = gol_font.render("GOOOOOOOOL!", True, "yellow")


ball = pygame.Rect(0, 0, 30, 30)
ball.center = (largura / 2, altura / 2)

#Players
cpu = pygame.Rect(0, 0, 20, 100)
cpu.centery = altura / 2
player = pygame.Rect(0, 0, 20, 100)
player.midright = (largura, altura / 2)


ball_speed_x = 6
ball_speed_y = 6
player_speed = 0
cpu_speed = 6
cpu_points = 0
player_points = 0


jogo_parado = False
tempo_gol = 0
TEMPO_GOL_MS = 18000

#Funções
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (largura / 2, random.randint(50, altura - 50))
    ball_speed_x *= random.choice([-1, 1])
    ball_speed_y *= random.choice([-1, 1])

def point_won(winner):
    global cpu_points, player_points, jogo_parado, tempo_gol

    if winner == "cpu":
        cpu_points += 1
    else:
        player_points += 1

    jogo_parado = True
    tempo_gol = pygame.time.get_ticks()

#ANIMAÇÃO GOL (BARULHO)

    # pygame.mixer.music.stop()
    # barulho_gol.stop()
    # barulho_gol.play()
    # pygame.mixer.music.stop()

def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= altura:
        ball_speed_y *= -1

    if ball.right >= largura:
        point_won("cpu")

    if ball.left <= 0:
        point_won("player")

    if ball.colliderect(player) or ball.colliderect(cpu):
        ball_speed_x *= -1

def animate_player():
    player.y += player_speed
    player.top = max(player.top, 0)
    player.bottom = min(player.bottom, altura)

def animate_cpu():
    cpu_speed = 5
    if cpu.centery < ball.centery:
        cpu.y += cpu_speed
    elif cpu.centery > ball.centery:
        cpu.y -= cpu_speed

    if cpu.top <= 0:
        cpu.top = 0
    if cpu.bottom >= altura:
        cpu.bottom = altura

#Loop Principal
while True:
    tela.fill((0, 220, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -6
            if event.key == pygame.K_DOWN:
                player_speed = 6

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player_speed = 0


    if not jogo_parado:
        animate_ball()
        animate_player()
        animate_cpu()
    else:
        if pygame.time.get_ticks() - tempo_gol >= TEMPO_GOL_MS:
            jogo_parado = False
            reset_ball()
           
           #MUSICA GOL
            # pygame.mixer.music.play(-1)

    #Arena
    cpu_score_surface = score_font.render(str(cpu_points), True, "white")
    player_score_surface = score_font.render(str(player_points), True, "white")
    tela.blit(cpu_score_surface, (largura / 4, 20))
    tela.blit(player_score_surface, (3 * largura / 4, 20))

    pygame.draw.aaline(tela, 'white', (largura / 2, 0), (largura / 2, altura))
    pygame.draw.ellipse(tela, 'white', ball)
    pygame.draw.rect(tela, 'white', cpu)
    pygame.draw.rect(tela, 'white', player)

    
    if jogo_parado:
        texto_rect = texto_gol.get_rect(center=(largura / 2, altura / 2))
        tela.blit(texto_gol, texto_rect)

    pygame.display.update()
    clock.tick(60)