import pygame
import random
import os

# --- CONFIGURAÇÕES INICIAIS ---
pygame.init()
pygame.mixer.init()
LARGURA, ALTURA = 800, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Dino Run - Vecna Edition")
clock = pygame.time.Clock()

# Cores e Constantes
BRANCO, PRETO, CINZA = (255, 255, 255), (0, 0, 0), (127, 140, 141)
VERMELHO = (231, 76, 60)
GRAVIDADE = 0.8
CHAO_Y = ALTURA - 50
ARQUIVO_HS = "highscore.txt"

# --- CARREGAMENTO DE ASSETS ---
som_pulo = pygame.mixer.Sound(os.path.join("assets", "jump.wav"))
som_morte = pygame.mixer.Sound(os.path.join("assets", "die.wav"))
som_ponto = pygame.mixer.Sound(os.path.join("assets", "point.wav")) # Novo som

# Música de fundo
pygame.mixer.music.load(os.path.join("assets", "stranger_things_trilha.mp3"))
pygame.mixer.music.set_volume(0.3)  # Volume entre 0.0 e 1.0
pygame.mixer.music.play(-1)  # -1 = loop infinito

fundo_img = pygame.image.load(os.path.join("assets", "fundo-lento2.png")).convert()
fundo_img = pygame.transform.scale(fundo_img, (LARGURA, ALTURA))
largura_fundo = fundo_img.get_width()

# --- CLASSES ---

class Dino:
    def __init__(self):
        self.frames_corrida = [
            pygame.image.load(os.path.join("assets", f"{i}corrida.png")).convert_alpha()
            for i in [1, 2, 3]
        ]
        self.img_pula = pygame.image.load(os.path.join("assets", "pula.png")).convert_alpha()
        self.img_agacha = pygame.image.load(os.path.join("assets", "agacha.png")).convert_alpha()
        self.img_agacha_mais = pygame.image.load(os.path.join("assets", "agacha_mais.png")).convert_alpha()
        self.img_morto = pygame.image.load(os.path.join("assets", "morto.png")).convert_alpha()

        self.tamanho_normal = (50, 60)
        self.tamanho_agachado = (60, 30) 
        
        self.frames_corrida = [pygame.transform.scale(img, self.tamanho_normal) for img in self.frames_corrida]
        self.img_pula = pygame.transform.scale(self.img_pula, self.tamanho_normal)
        self.img_agacha = pygame.transform.scale(self.img_agacha, self.tamanho_agachado)
        self.img_agacha_mais = pygame.transform.scale(self.img_agacha_mais, self.tamanho_agachado)
        self.img_morto = pygame.transform.scale(self.img_morto, (60, 50))

        self.image = self.frames_corrida[0]
        self.rect = self.image.get_rect(topleft=(50, CHAO_Y - 60))
        self.hitbox = self.rect.inflate(-20, -10)
        self.vel_y = 0
        self.no_chao = True
        self.agachado = False
        self.step_index = 0.0

    def pular(self):
        if self.no_chao and not self.agachado:
            self.vel_y = -15
            self.no_chao = False
            som_pulo.play()

    def cancelar_pulo(self):
        if self.vel_y < -7:
            self.vel_y = -7

    def agachar(self, apertou):
        self.agachado = apertou

    def atualizar(self, velocidade_atual, morto=False):
        if morto:
            self.image = self.img_morto
            return

        self.vel_y += GRAVIDADE
        self.rect.y += self.vel_y
        if self.rect.bottom >= CHAO_Y:
            self.rect.bottom, self.vel_y, self.no_chao = CHAO_Y, 0, True

        self.step_index += velocidade_atual * 0.025 
        
        if not self.no_chao:
            self.image = self.img_pula
            self.rect.height = self.tamanho_normal[1]
            self.hitbox = self.rect.inflate(-15, -10)
        elif self.agachado:
            self.image = self.img_agacha if int(self.step_index) % 2 == 0 else self.img_agacha_mais
            self.rect.height = self.tamanho_agachado[1]
            self.rect.bottom = CHAO_Y
            self.hitbox = self.rect.inflate(-10, -5)
        else:
            indice = int(self.step_index) % len(self.frames_corrida)
            self.image = self.frames_corrida[indice]
            self.rect.height = self.tamanho_normal[1]
            self.rect.bottom = CHAO_Y
            self.hitbox = self.rect.inflate(-20, -10)

    def desenhar(self, surface):
        surface.blit(self.image, self.rect)

class Obstaculo:
    def __init__(self, tipo):
        self.tipo = tipo
        self.step_index = 0  
        if tipo == "vinha":
            self.image = pygame.image.load(os.path.join("assets", "vinha.png")).convert_alpha()
            self.image = pygame.transform.scale(self.image, (75, 50))
            self.rect = self.image.get_rect(midbottom=(LARGURA + 100, CHAO_Y))
            self.hitbox_offset = (-25, -20)
        elif tipo == "relogio":
            self.image = pygame.image.load(os.path.join("assets", "relogio.png")).convert_alpha()
            self.image = pygame.transform.scale(self.image, (50, 75))
            self.rect = self.image.get_rect(midbottom=(LARGURA + 100, CHAO_Y))
            self.hitbox_offset = (-10, -5)
        elif tipo == "demobat":
            self.frames = [pygame.image.load(os.path.join("assets", f"demobat{i}.png")).convert_alpha() for i in [1, 2, 3, 4]]
            self.frames = [pygame.transform.scale(img, (60, 90)) for img in self.frames]
            self.image = self.frames[0]
            self.rect = self.image.get_rect(midbottom=(LARGURA + 100, CHAO_Y - 30))
            self.hitbox_offset = (-35, -45)
        
        # Cria a hitbox inicial
        self.hitbox = self.rect.inflate(*self.hitbox_offset)

    def mover(self, vel):
        self.rect.x -= vel
        if self.tipo == "demobat":
            self.step_index += 0.2
            if self.step_index >= len(self.frames): self.step_index = 0
            self.image = self.frames[int(self.step_index)]
        
        self.hitbox = self.rect.inflate(*self.hitbox_offset)

    def desenhar(self, surface):
        surface.blit(self.image, self.rect)
        #pygame.draw.rect(surface, (255,0,0), self.hitbox, 2) # Desenha a hitbox para debug

# Partículas de Cinza (Upside Down Effect)
class Cinza:
    def __init__(self):
        self.x = random.randint(0, LARGURA)
        self.y = random.randint(0, ALTURA)
        self.vel_x = random.uniform(-1, -3)
        self.vel_y = random.uniform(0.5, 1.5)
        self.tamanho = random.randint(1, 3)

    def atualizar(self):
        self.x += self.vel_x
        self.y += self.vel_y
        if self.x < 0: self.x = LARGURA
        if self.y > ALTURA: self.y = 0

    def desenhar(self, surface):
        pygame.draw.circle(surface, CINZA, (int(self.x), int(self.y)), self.tamanho)

# --- SISTEMA ---
def carregar_highscore():
    if os.path.exists(ARQUIVO_HS):
        with open(ARQUIVO_HS, "r") as f:
            try: return int(f.read())
            except: return 0
    return 0

def salvar_highscore(score):
    with open(ARQUIVO_HS, "w") as f: f.write(str(score))

def resetar_jogo():
    # dino, obstaculos, cinzas, bg_x, timer, vel, pontos, game_over
    c = [Cinza() for _ in range(40)]
    return Dino(), [], c, 0, 0, 7, 0, False

# --- LOOP PRINCIPAL ---
dino, obstaculos, cinzas, bg_x, timer_spawn, vel_jogo, pontos, game_over = resetar_jogo()
high_score = carregar_highscore()
fonte = pygame.font.SysFont("Arial", 22, bold=True)
fonte_grande = pygame.font.SysFont("Arial", 55, bold=True)

rodando = True
while rodando:
    # 1. Background e Parallax
    tela.blit(fundo_img, (bg_x, 0))
    tela.blit(fundo_img, (largura_fundo + bg_x, 0))
    
    for c in cinzas:
        c.atualizar()
        c.desenhar(tela)
    
    if not game_over:
        bg_x -= vel_jogo * 0.3 
        if bg_x <= -largura_fundo: bg_x = 0

    # 2. Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key in [pygame.K_SPACE, pygame.K_UP]:
                if game_over:
                    dino, obstaculos, cinzas, bg_x, timer_spawn, vel_jogo, pontos, game_over = resetar_jogo()
                else: dino.pular()
            if evento.key == pygame.K_r and game_over:
                dino, obstaculos, cinzas, bg_x, timer_spawn, vel_jogo, pontos, game_over = resetar_jogo()
        if evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_SPACE, pygame.K_UP]: dino.cancelar_pulo()

    # 3. Lógica
    if not game_over:
        teclas = pygame.key.get_pressed()
        dino.agachar(teclas[pygame.K_DOWN])
        dino.atualizar(vel_jogo)
        
        timer_spawn += 1
        if timer_spawn > random.randint(45, 90):
            tipo = random.choice(["vinha", "relogio", "demobat"])
            obstaculos.append(Obstaculo(tipo))
            timer_spawn = 0

        for obs in obstaculos[:]:
            obs.mover(vel_jogo)
            if dino.hitbox.colliderect(obs.hitbox):
                game_over = True
                som_morte.play()
                if pontos > high_score:
                    high_score = pontos
                    salvar_highscore(high_score)
            if obs.rect.right < 0:
                obstaculos.remove(obs)
                pontos += 1
                if pontos > 0 and pontos % 100 == 0: som_ponto.play() # Som a cada 100 pts
                vel_jogo += 0.05
    else:
        dino.atualizar(vel_jogo, morto=True)

    # 4. Desenhos e UI
    pygame.draw.line(tela, PRETO, (0, CHAO_Y), (LARGURA, CHAO_Y), 3)
    dino.desenhar(tela)
    for obs in obstaculos: obs.desenhar(tela)

    txt_p = fonte.render(f"SCORE: {int(pontos)}", True, PRETO)
    txt_h = fonte.render(f"HI: {int(high_score)}", True, CINZA)
    tela.blit(txt_p, (LARGURA - 140, 20))
    tela.blit(txt_h, (LARGURA - 250, 20))

    if game_over:
        msg = fonte_grande.render("GAME OVER", True, VERMELHO)
        tela.blit(msg, (LARGURA//2 - msg.get_width()//2, ALTURA//2 - 60))
        msg_r = fonte.render("Pressione ESPAÇO ou R para Reiniciar", True, BRANCO)
        tela.blit(msg_r, (LARGURA//2 - msg_r.get_width()//2, ALTURA//2 + 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()