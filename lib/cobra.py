import pygame


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
            self.posx -= 1

        if buttons[pygame.K_d]:
            self.posx += 1

        if buttons[pygame.K_w]:
            self.posy -= 1

        if buttons[pygame.K_s]:
            self.posy += 1

        self.rect.center = (self.posx, self.posy)  # type: ignore
