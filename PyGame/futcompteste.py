import pygame, sys, random
pygame.init()
pygame.mixer.init()

#JANELA
largura = 1280
altura = 720
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

# --- CARREGAMENTO DE IMAGENS E FONTES DO MENU ---
pygame.display.set_caption("MENU")

# 1. Ajuste perfeito da tela de fundo
tela_de_fundo_orig = pygame.image.load("planodefundo.png")
tela_de_fundo = pygame.transform.scale(tela_de_fundo_orig, (largura, altura))

# 2. Carregar imagem do botão
img_botao_raw = pygame.image.load("botãoplay.png") 
img_botao = pygame.transform.scale(img_botao_raw, (300, 110))

# 3. Carregar Fonte TickerBit (O arquivo Tickerbit.ttf deve estar na pasta)
try:
    font_botao = pygame.font.Font("Tickerbit.ttf", 50) 
except:
    font_botao = pygame.font.Font(None, 60)

def menu_principal(): 
    pygame.display.set_caption("MENU")

    rect_play = img_botao.get_rect(center=(largura/2, altura/2 - 60))
    rect_sair = img_botao.get_rect(center=(largura/2, altura/2 + 70))

    txt_play = font_botao.render("PLAY", True, "white")
    txt_sair = font_botao.render("SAIR", True, "white")

    rect_txt_play = txt_play.get_rect(center=rect_play.center)
    rect_txt_sair = txt_sair.get_rect(center=rect_sair.center)

    while True:
        tela.blit(tela_de_fundo, (0, 0))
        
        tela.blit(img_botao, rect_play)
        tela.blit(img_botao, rect_sair)

        tela.blit(txt_play, rect_txt_play)
        tela.blit(txt_sair, rect_txt_sair)

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_play.collidepoint(mouse_pos):
                    jogar()
                
                if rect_sair.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

#MÚSICAS
pygame.mixer.music.load('Vinheta Fox Sports Brasil.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

barulho_gol = pygame.mixer.Sound('toca-a-musica-do-fox-sports.mp3')
barulho_gol.set_volume(0.5)


#FONTES 
score_font = pygame.font.Font(None, 100)
gol_font = pygame.font.Font(None, 140)
timer_font = pygame.font.Font(None, 50)

texto_gol = gol_font.render("GOOOOOOOOL!", True, "yellow")

#TEMPO DA PARTIDA 
TEMPO_PARTIDA = 60 
inicio_partida = pygame.time.get_ticks()

#ESTADOS
JOGANDO = 0
RESULTADO = 1
estado_jogo = JOGANDO

#OBJETOS
ball = pygame.Rect(0, 0, 30, 30)
ball.center = (largura / 2, altura / 2)

cpu = pygame.Rect(0, 0, 20, 100)
cpu.centery = altura / 2

player = pygame.Rect(0, 0, 20, 100)
player.midright = (largura, altura / 2)

#VARIÁVEIS
ball_speed_x = 6
ball_speed_y = 6
player_speed = 0
cpu_speed = 6

cpu_points = 0
player_points = 0

jogo_parado = False
tempo_gol = 0
TEMPO_GOL_MS = 3000

#FUNÇÕES
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

    pygame.mixer.music.stop()
    barulho_gol.stop()
    barulho_gol.play()

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
    # Esta função lê a variável global player_speed
    player.y += player_speed
    player.top = max(player.top, 0)
    player.bottom = min(player.bottom, altura)

def animate_cpu():
    cpu_speed = 5
    if cpu.centery < ball.centery:
        cpu.y += cpu_speed
    elif cpu.centery > ball.centery:
        cpu.y -= cpu_speed

    cpu.top = max(cpu.top, 0)
    cpu.bottom = min(cpu.bottom, altura)

def tela_resultado():
    tela.fill((0, 120, 0))

    fim = score_font.render("FIM DE JOGO", True, "yellow")
    placar = score_font.render(f"{player_points}  x  {cpu_points}", True, "white")

    if player_points > cpu_points:
        vencedor = "VOCÊ VENCEU!"
    elif cpu_points > player_points:
        vencedor = "CPU VENCEU!"
    else:
        vencedor = "EMPATE!"

    vencedor_txt = score_font.render(vencedor, True, "white")
    instrucao = timer_font.render("R - Reiniciar | ESC - Sair", True, "white")

    tela.blit(fim, (largura//2 - 220, 100))
    tela.blit(placar, (largura//2 - 150, 250))
    tela.blit(vencedor_txt, (largura//2 - 220, 380))
    tela.blit(instrucao, (largura//2 - 200, 520))

#LOOP PRINCIPAL
def jogar(): 
    # --- CORREÇÃO AQUI: adicionei player_speed ao global ---
    global cpu_points, player_points, inicio_partida, estado_jogo, jogo_parado, player_speed
    
    cpu_points = 0
    player_points = 0
    estado_jogo = JOGANDO
    jogo_parado = False
    player_speed = 0 # Garante que começa parado
    inicio_partida = pygame.time.get_ticks()
    reset_ball()
    pygame.mixer.music.play(-1)

    pygame.display.set_caption("FutCOMP")
   
    while True:
        tela.fill((0, 220, 0))

        tempo_atual = pygame.time.get_ticks()
        tempo_passado = (tempo_atual - inicio_partida) // 1000
        tempo_restante = max(0, TEMPO_PARTIDA - tempo_passado)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if estado_jogo == JOGANDO:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_speed = -6
                    if event.key == pygame.K_DOWN:
                        player_speed = 6

                if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_UP, pygame.K_DOWN):
                        player_speed = 0

            if estado_jogo == RESULTADO:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        cpu_points = 0
                        player_points = 0
                        inicio_partida = pygame.time.get_ticks()
                        estado_jogo = JOGANDO
                        pygame.mixer.music.play(-1)

                    if event.key == pygame.K_ESCAPE:
                        return 

        if estado_jogo == JOGANDO:
            if not jogo_parado:
                animate_ball()
                animate_player()
                animate_cpu()
            else:
                if pygame.time.get_ticks() - tempo_gol >= TEMPO_GOL_MS:
                    jogo_parado = False
                    reset_ball()
                    pygame.mixer.music.play(-1)

            if tempo_restante == 0:
                estado_jogo = RESULTADO
                pygame.mixer.music.stop()

            #HUD
            tela.blit(score_font.render(str(cpu_points), True, "white"), (largura/4, 20))
            tela.blit(score_font.render(str(player_points), True, "white"), (3*largura/4, 20))
            tela.blit(timer_font.render(f"{tempo_restante}", True, "white"), (largura/2 - 20, 20))

            pygame.draw.aaline(tela, 'white', (largura/2, 0), (largura/2, altura))
            pygame.draw.ellipse(tela, 'white', ball)
            pygame.draw.rect(tela, 'white', cpu)
            pygame.draw.rect(tela, 'white', player)

            if jogo_parado:
                tela.blit(texto_gol, texto_gol.get_rect(center=(largura/2, altura/2)))

        else:
            tela_resultado()

        pygame.display.update()
        clock.tick(60)

# --- EXECUÇÃO ---
menu_principal()