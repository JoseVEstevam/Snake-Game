
import pygame
import sys
from math import ceil
from lib.cobra import Cobra
from lib.maca import Maca
from lib.botoes import Botao
from lib.ponteiro import Ponteiro


class Jogo():

    def __init__(self) -> None:
        self.estado = 'menu'
        pygame.mouse.set_visible(False)

    def menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                ponteiro.som.play()
            if event.type == pygame.MOUSEBUTTONUP:
                self.estado = 'principal'

        DISPLAY.blit(BACKGROUND_MENU, (0, 0))
        grupo_botao.draw(DISPLAY)

        ponteiro_grupo.draw(DISPLAY)
        ponteiro_grupo.update()

        pygame.display.flip()

    def principal(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.preencher_tela()

        grupo_maca.draw(DISPLAY)

        grupo_cobra.draw(DISPLAY)
        grupo_cobra.update()

        pygame.display.flip()

    def controle_tela(self):
        if self.estado == 'menu':
            self.menu()
        elif self.estado == 'principal':
            self.principal()

    @staticmethod
    def preencher_tela():
        for x in range(ceil(DISPLAY_X / BACKGROUND_X)):
            for y in range(ceil(DISPLAY_Y / BACKGROUND_Y)):
                DISPLAY.blit(BACKGROUND_JOGO,
                             (x * BACKGROUND_X, y * BACKGROUND_Y))


pygame.init()

# Cores
WHITE = (255, 255, 255)

# Configurações da janela
DISPLAY_X = 1280
DISPLAY_Y = 720
DISPLAY = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))

# Ponteiro do mouse
ponteiro_grupo = pygame.sprite.Group()
ponteiro = Ponteiro("gfx/mouse.png")
ponteiro_grupo.add(ponteiro)

# Configurações da tela de fundo menu
BACKGROUND_MENU = pygame.image.load("gfx/menu_background.jpg")

# Configurações dos botões menu
grupo_botao = pygame.sprite.Group()

botao_play = Botao(300, 75, (WHITE), (int(
    DISPLAY_X / 2), int(DISPLAY_Y / 2) + 75))

grupo_botao.add(botao_play)

# Configurações da tela de fundo jogo
BACKGROUND_JOGO = pygame.image.load("gfx/background.png")
BACKGROUND_X = BACKGROUND_JOGO.get_width()
BACKGROUND_Y = BACKGROUND_JOGO.get_height()

# Configurações da Cobra
cobra_x = int(DISPLAY_X / 2 - 35 / 2)
cobra_y = int(0.80 * DISPLAY_Y)
cobra = Cobra(35, 35, (138, 154, 91), (cobra_x, cobra_y))
grupo_cobra = pygame.sprite.Group()
grupo_cobra.add(cobra)

# Configurações maçã
maca = Maca(35, 35, (255, 0, 0), (500, 200))
grupo_maca = pygame.sprite.Group()
grupo_maca.add(maca)

# Configurações gerais
clock = pygame.time.Clock()
jogo = Jogo()

while True:

    jogo.controle_tela()

    clock.tick(60)
