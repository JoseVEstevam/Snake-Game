import pygame


class Ponteiro(pygame.sprite.Sprite):

    def __init__(self, caminho) -> None:
        super().__init__()
        self.image = pygame.image.load(caminho)
        self.rect = self.image.get_rect()
        self.rect.topleft = pygame.mouse.get_pos()
        self.som = pygame.mixer.Sound("sfx/click.wav")

    def update(self):
        self.rect.topleft = pygame.mouse.get_pos()  # type: ignore
