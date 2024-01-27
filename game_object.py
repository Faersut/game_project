import rooms
import pygame


class GameObject:
    def __init__(self):
        self.img = None
        self.rect = None
        self.pos_x = 0
        self.pos_y = 0
        self.width = 0
        self.height = 0

    def set_image(self, img):
        self.img = pygame.image.load(img)
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def set_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.rect.y = y
        self.rect.x = x

    def set_size(self, width, height):
        self.width = width
        self.height = height
        pygame.transform.scale(self.img, (self.width, self.height))
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def render(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))


class Player(GameObject):
    def __init__(self):
        super().__init__()

        self.skins = []
        self.speed = 5
        self.hp = 100

        self.press_down = False
        self.press_up = False
        self.press_left = False
        self.press_right = False

        self.is_collide = False

    def set_skins(self, *skins):
        self.skins = [
            pygame.image.load(skins[0]),
            pygame.image.load(skins[1])
        ]

    def set_base_img(self, img):
        self.img = pygame.image.load(img)
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def update(self, event, rects, room):
        new_x, new_y = self.pos_x, self.pos_y

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.press_up = True
            if event.key == pygame.K_s:
                self.press_down = True
            if event.key == pygame.K_d:
                self.img = self.skins[0]
                self.press_right = True
            if event.key == pygame.K_a:
                self.img = self.skins[1]
                self.press_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.press_up = False
            if event.key == pygame.K_s:
                self.press_down = False
            if event.key == pygame.K_d:
                self.press_right = False
            if event.key == pygame.K_a:
                self.press_left = False

        if self.press_down:
            new_y += self.speed
        if self.press_up:
            new_y -= self.speed
        if self.press_right:
            new_x += self.speed
        if self.press_left:
            new_x -= self.speed

        for rect in rects:
            if pygame.Rect(new_x, new_y, self.width, self.height).colliderect(rect):
                self.is_collide = True

        if isinstance(room, rooms.StartRoom):
            if new_y <= 45 or new_x <= 0 or new_x + self.width >= 800:
                self.is_collide = True

        if self.is_collide:
            self.press_down = False
            self.press_up = False
            self.press_left = False
            self.press_right = False

        if not self.is_collide:
            if self.press_down:
                self.pos_y += self.speed
                self.rect.y += self.speed
            if self.press_up:
                self.pos_y -= self.speed
                self.rect.y -= self.speed
            if self.press_right:
                self.pos_x += self.speed
                self.rect.x += self.speed
            if self.press_left:
                self.pos_x -= self.speed
                self.rect.x -= self.speed

        self.is_collide = False
