import pygame


class Maca(pygame.sprite.Sprite):

    def __init__(self, width, height, color, pos: tuple) -> None:
        super().__init__()
        self.posx, self.posy = pos
        self.image = pygame.surface.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.posx, self.posy)
