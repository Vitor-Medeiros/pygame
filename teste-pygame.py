import pygame
import sys
import random

pygame.init()


largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('janela')

PRETO = (0,0,0)

BRANCO = (255,255,255)

tamanho_fonte = 45
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render('Vitor', True, BRANCO)
novoTexto = fonte.render('Bortot', True, BRANCO)

texto_rect = texto.get_rect()
texto_rect.x = random.randint(0, largura - texto_rect.width)
texto_rect.y = random.randint(0, altura - texto_rect.height)

novoTexto_rect = novoTexto.get_rect()
novoTexto_rect.x = random.randint(0, largura - novoTexto_rect.width)
novoTexto_rect.y = random.randint(0, altura - novoTexto_rect.height)

clock = pygame.time.Clock()

velocidade_x1 = random.randint(-2,2)
velocidade_y1 = random.randint(-2,2)

velocidade_x2 = random.randint(-2,2)
velocidade_y2 = random.randint(-2,2)

while velocidade_x1 == 0 and velocidade_y1 == 0:
    velocidade_x1 = random.randint(-2,2)
    velocidade_y1 = random.randint(-2,2)

while velocidade_x2 == 0 and velocidade_y2 == 0:
    velocidade_x2 = random.randint(-2,2)
    velocidade_y2 = random.randint(-2,2)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    bateu = False
    tela.fill(PRETO)

    texto_rect.x += velocidade_x1
    texto_rect.y += velocidade_y1

    novoTexto_rect.x += velocidade_x2
    novoTexto_rect.y += velocidade_y2

    if texto_rect.right >= largura:
        texto_rect.right = largura
        velocidade_x1 = random.randint(-2,0)
        velocidade_y1 = random.randint(-2,2)
        bateu = True

    if texto_rect.left <= 0:
        texto_rect.left = 0
        velocidade_x1 = random.randint(0,2)
        velocidade_y1 = random.randint(-2,2)
        bateu = True

    if texto_rect.top <= 0:
        texto_rect.top = 0
        velocidade_x1 = random.randint(-2,2)
        velocidade_y1 = random.randint(0,2)
        bateu = True

    if texto_rect.bottom >= altura:
        texto_rect.bottom = altura
        velocidade_x1 = random.randint(-2,2)
        velocidade_y1 = random.randint(-2,0)
        bateu = True

    if novoTexto_rect.right >= largura:
        novoTexto_rect.right = largura
        velocidade_x2 = random.randint(-2,0)
        velocidade_y2 = random.randint(-2,2)
        bateu = True

    if novoTexto_rect.left <= 0:
        novoTexto_rect.left = 0
        velocidade_x2 = random.randint(0,2)
        velocidade_y2 = random.randint(-2,2)
        bateu = True

    if novoTexto_rect.top <= 0:
        novoTexto_rect.top = 0
        velocidade_x2 = random.randint(-2,2)
        velocidade_y2 = random.randint(0,2)
        bateu = True

    if novoTexto_rect.bottom >= altura:
        novoTexto_rect.bottom = altura
        velocidade_x2 = random.randint(-2,2)
        velocidade_y2 = random.randint(-2,0)
        bateu = True

    if texto_rect.colliderect(novoTexto_rect):
        velocidade_x1 = random.randint(-2,2)
        velocidade_y1 = random.randint(-2,2)
        velocidade_x2 = random.randint(-2,2)
        velocidade_y2 = random.randint(-2,2)
        bateu = True

    if bateu:
        cor_atual = (
            random.randint(1,255),
            random.randint(1,255),
            random.randint(1,255)
        )
        texto = fonte.render('Vitor', True, cor_atual)
        novoTexto = fonte.render('Bortot', True, cor_atual)

    tela.blit(texto, texto_rect)
    tela.blit(novoTexto, novoTexto_rect)

    clock.tick(240)
    pygame.display.flip()
pygame.quit()
sys.exit()