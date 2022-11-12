import pygame


class Botao(pygame.sprite.Sprite):

    def __init__(self, caminho, pos: tuple):
        super().__init__()
        self.posx, self.posy = pos
        self.image = pygame.image.load(caminho)
        self.rect = self.image.get_rect()
        self.rect.center = (self.posx, self.posy)


class BotaoCobra(pygame.sprite.Sprite):

    def __init__(self, caminho, pos: tuple):
        super().__init__()
        self.posx, self.posy = pos
        self.image = pygame.image.load(caminho)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.posx, self.posy)
