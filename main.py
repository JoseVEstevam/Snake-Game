
import pygame
import sys
from math import ceil
from lib.atores import Cobra, Maca
from lib.botoes import Botao, BotaoCobra
from lib.ponteiro import Ponteiro


class Jogo():

    def __init__(self) -> None:
        self.estado = 'menu'
        pygame.mouse.set_visible(False)
        # pygame.mixer.music.load("")  # Adicionar música
        # pygame.mixer.music.play()

    def menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                ponteiro.som.play()
                if pygame.sprite.spritecollide(ponteiro, grupo_botao, False):
                    self.estado = 'principal'

        DISPLAY.blit(BACKGROUND_MENU, (0, 0))
        grupo_botao.draw(DISPLAY)
        grupo_cobra_menu.draw(DISPLAY)

        ponteiro_grupo.draw(DISPLAY)
        ponteiro_grupo.update()

        pygame.display.flip()

    def principal(self):
        # pygame.mixer.music.stop()
        pontuacao = 0
        tamanho_cobra = 3
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.preencher_tela()
        self.bordas()

        grupo_maca.draw(DISPLAY)

        grupo_cobra.draw(DISPLAY)
        grupo_cobra.update()

        if pygame.sprite.collide_rect(cobra, maca):
            pontuacao += 1
            tamanho_cobra += 1
            grupo_maca.update()

        pygame.display.flip()

    def pausa(self):
        pass

    def controle_tela(self):
        if self.estado == 'menu':
            self.menu()
        elif self.estado == 'principal':
            self.principal()
        elif self.estado == 'pausa':
            self.pausa()

    @staticmethod
    def preencher_tela():
        for x in range(ceil(DISPLAY_X / BACKGROUND_X)):
            for y in range(ceil(DISPLAY_Y / BACKGROUND_Y)):
                DISPLAY.blit(BACKGROUND_JOGO,
                             (x * BACKGROUND_X, y * BACKGROUND_Y))

    @staticmethod
    def bordas():
        for x in range(ceil(DISPLAY_X / PEDRA_X)):
            for y in range(ceil(DISPLAY_Y / PEDRA_Y)):
                if x == 0:
                    DISPLAY.blit(PEDRA, (x * PEDRA_X, y * PEDRA_Y))
                if y == 0:
                    DISPLAY.blit(PEDRA, (x * PEDRA_X, y * PEDRA_Y))
                if x == 27:
                    DISPLAY.blit(PEDRA, (x * PEDRA_X, y * PEDRA_Y))
                if y == 20:
                    DISPLAY.blit(PEDRA, (x * PEDRA_X, y * PEDRA_Y))


pygame.init()

# Cores
WHITE = (255, 255, 255)

# Configurações da janela
DISPLAY_X = 1260
DISPLAY_Y = 710
DISPLAY = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))

# Ponteiro do mouse
ponteiro_grupo = pygame.sprite.Group()
ponteiro = Ponteiro("gfx/mouse.png")
ponteiro_grupo.add(ponteiro)

# Configurações da tela de fundo menu
BACKGROUND_MENU = pygame.image.load("gfx/menu_background.jpg")

# Configurações dos botões menu
cobra_menu = BotaoCobra("gfx/cobra_menu.png", (440, 400))
grupo_cobra_menu = pygame.sprite.Group()
grupo_cobra_menu.add(cobra_menu)

grupo_botao = pygame.sprite.Group()
botao_play = Botao(
    "gfx/play.png", (int(DISPLAY_X / 2), int(DISPLAY_Y / 2) + 90))
grupo_botao.add(botao_play)

# Configurações da tela de fundo jogo
BACKGROUND_JOGO = pygame.image.load("gfx/background.png")
BACKGROUND_X = BACKGROUND_JOGO.get_width()
BACKGROUND_Y = BACKGROUND_JOGO.get_height()

# Configurações da Cobra
cobra_x = int(DISPLAY_X - (0.8 * DISPLAY_X))
cobra_y = int(0.8 * DISPLAY_Y)
cobra = Cobra((cobra_x, cobra_y), 4)
grupo_cobra = pygame.sprite.Group()
grupo_cobra.add(cobra)

# Configurações maçã
maca = Maca(DISPLAY_X, DISPLAY_Y)
grupo_maca = pygame.sprite.Group()
grupo_maca.add(maca)

# Configurações bordas
PEDRA = pygame.image.load("gfx/pedra.png")
PEDRA_X = PEDRA.get_width()
PEDRA_Y = PEDRA.get_height()

# Configurações gerais
clock = pygame.time.Clock()
jogo = Jogo()

# Jogo
while True:

    jogo.controle_tela()

    clock.tick(60)
