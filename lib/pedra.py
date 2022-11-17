import pygame


class PedraBorda(pygame.sprite.Sprite):

    def __init__(self, caminho) -> None:
        super().__init__()
        self.image = pygame.image.load(caminho)
        self.rect = self.image.get_rect()
