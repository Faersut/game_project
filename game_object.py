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
        self.img = pygame.image.load(img).convert_alpha()

    def set_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.rect = pygame.Rect((self.pos_x, self.pos_y), (self.width, self.height))

    def set_size(self, width, height):
        self.width = width
        self.height = height
        pygame.transform.scale(self.img, (self.width, self.height))
        self.rect = pygame.Rect((self.pos_x, self.pos_y), (self.width, self.height))

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
            pygame.image.load(skins[0]).convert_alpha(),
            pygame.image.load(skins[1]).convert_alpha()
        ]

    def set_base_img(self, img):
        self.img = pygame.image.load(img).convert_alpha()
        self.rect = pygame.Rect((self.pos_x, self.pos_y), (self.width, self.height))

    def update(self, event):
        keys = pygame.key.get_pressed()
        current_x, current_y = self.pos_x, self.pos_y
        self.pos_x += (keys[pygame.K_d] - keys[pygame.K_a]) * self.speed
        self.pos_y += (keys[pygame.K_s] - keys[pygame.K_w]) * self.speed
        if self.is_collide:
            self.pos_x = current_x
            self.pos_y = current_y

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.img = self.skins[0]
            if event.key == pygame.K_a:
                self.img = self.skins[1]

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def collide_detected(self, rects):
        for rect in rects:
            if self.rect.colliderect(rect):
                self.is_collide = True
        self.is_collide = False
