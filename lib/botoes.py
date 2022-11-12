import pygame


class Botao(pygame.sprite.Sprite):

    def __init__(self, width, heigth, color, pos: tuple):
        super().__init__()
        self.posx, self.posy = pos
        self.image = pygame.surface.Surface((width, heigth))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.posx, self.posy)
