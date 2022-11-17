import pygame
from random import randint


class Cobra(pygame.sprite.Sprite):

    def __init__(self, width, height, color, pos: tuple) -> None:
        super().__init__()
        self.posx, self.posy = pos
        self.image = pygame.surface.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.posx, self.posy)

    def update(self) -> None:
        buttons = pygame.key.get_pressed()
        if buttons[pygame.K_a]:
            self.posx -= 10

        if buttons[pygame.K_d]:
            self.posx += 10

        if buttons[pygame.K_w]:
            self.posy -= 10

        if buttons[pygame.K_s]:
            self.posy += 10

        self.rect.center = (self.posx, self.posy)  # type: ignore


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
