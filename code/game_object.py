import pygame


class GameObject:
    def __init__(self):
        self.img = None
        self.rect = None
        self.pos_x = 0
        self.pos_y = 0
        self.wight = 0
        self.height = 0

    def set_image(self, img):
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()

    def set_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def set_size(self, width, height):
        self.wight = width
        self.height = height
        pygame.transform.scale(self.img, (self.wight, self.height))

    def render(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))