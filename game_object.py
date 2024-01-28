import random

import rooms
import pygame

GO_DANGEON = pygame.USEREVENT + 3
EXIT_DANGEON = pygame.USEREVENT + 4
FIRST_ARENA = pygame.USEREVENT + 5
SECOND_ARENA = pygame.USEREVENT + 6


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
        self.speed = 10
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

    def update(self, event, rects, room, enemy):
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

        player_rect = pygame.Rect(new_x, new_y, 75, 130)
        for rect in rects:
            if player_rect.colliderect(rect):
                if rect.width == 100 and rect.height == 100:
                    pygame.event.post(pygame.event.Event(EXIT_DANGEON))
                if rect.left == 100 and rect.width == 200 and rect.height == 100:
                    pygame.event.post(pygame.event.Event(FIRST_ARENA))
                if rect.left == 500 and rect.width == 200 and rect.height == 100:
                    pygame.event.post(pygame.event.Event(SECOND_ARENA))
                self.is_collide = True

        if new_x <= 0 or new_x + self.width >= 750:
            self.is_collide = True
        if new_y + self.height >= 510 and isinstance(room, rooms.Dangeon):
            self.is_collide = True

        if isinstance(room, rooms.Arena1) or isinstance(room, rooms.Arena2):
            if pygame.Rect(new_x, new_y, 75, 130).colliderect(enemy.rect):
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

        if self.pos_y >= 600 and isinstance(room, rooms.StartRoom):
            pygame.event.post(pygame.event.Event(GO_DANGEON))


class Skeleton(GameObject):
    def __init__(self):
        super().__init__()

        skeleton_img = pygame.image.load("data/arena1/skeleton_enemy.png")
        skeleton_img = pygame.transform.scale(skeleton_img, (120, 200))
        self.img = skeleton_img
        self.set_size(120, 200)
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.set_pos(350, 10)

        self.speed = 10
        self.arena_active = False

        self.direction_x = 0
        self.direction_y = 0

    def update(self):
        if self.arena_active:
            self.direction_x = random.choice([-1, 1])
            self.direction_y = random.choice([-1, 1])
            self.arena_active = False

        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.direction_y *= -1
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.direction_x *= -1
        self.pos_x += self.direction_x * self.speed
        self.pos_y += self.direction_y * self.speed
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
