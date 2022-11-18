import pygame
from random import randint


class Cobra(pygame.sprite.Sprite):

    def __init__(self, pos: tuple,  velocidade) -> None:
        super().__init__()
        self.velocidade = velocidade
        self.x, self.y = 5, 0
        self.posx, self.posy = pos
        self.cabeca: list = []
        self.cauda: list = []
        self.corpo: list = []
        self.cobra = pygame.image.load("gfx/snake_sprite.png")
        for y in range(2):
            for x in range(3, 5):
                img = self.cobra.subsurface((64 * x, 64 * y), (64, 64))
                img = pygame.transform.scale(
                    img, (64 * 0.8, 64 * 0.8))
                self.cabeca.append(img)
        self.index = 1
        self.image = self.cabeca[self.index]
        self.rect = self.image.get_rect()  # type: ignore
        self.rect.center = (self.posx, self.posy)

    def update(self) -> None:

        self.buttons = pygame.key.get_pressed()

        if self.x > 0:
            self.direita()
            self.cima()
            self.baixo()
        elif self.x < 0:
            self.esquerda()
            self.cima()
            self.baixo()

        if self.y > 0:
            self.esquerda()
            self.direita()
            self.baixo()
        elif self.y < 0:
            self.esquerda()
            self.direita()
            self.cima()

        self.posx += self.x
        self.posy += self.y

        self.image = self.cabeca[self.index]
        self.rect = self.image.get_rect()  # type: ignore
        self.rect.center = (self.posx, self.posy)  # type: ignore

    def colocar_corpo(self):
        pass

    def esquerda(self):
        if self.buttons[pygame.K_a]:
            self.index = 2
            self.y = 0
            self.x = -self.velocidade

    def direita(self):
        if self.buttons[pygame.K_d]:
            self.index = 1
            self.y = 0
            self.x = self.velocidade

    def cima(self):
        if self.buttons[pygame.K_w]:
            self.index = 0
            self.y = -self.velocidade
            self.x = 0

    def baixo(self):
        if self.buttons[pygame.K_s]:
            self.index = 3
            self.y = self.velocidade
            self.x = 0


class Maca(pygame.sprite.Sprite):

    def __init__(self, tela_x, tela_y) -> None:
        super().__init__()
        self.tela_x = tela_x
        self.tela_y = tela_y
        self.image = pygame.image.load("gfx/snake_sprite.png")
        self.image = self.image.subsurface((0, 192), (64, 64))
        self.image = pygame.transform.scale(self.image, (64 * 0.8, 64 * 0.8))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(77, self.tela_x - 77),
                            randint(77, self.tela_y - 77))

    def update(self) -> None:
        self.rect.center = (randint(77, self.tela_x - 77),  # type: ignore
                            randint(77, self.tela_y - 77))
