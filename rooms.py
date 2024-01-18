import pygame


class Room:
    def __init__(self):
        self.objects = []
        self.bg_img = None

    def add_objects(self, *obj):
        self.objects.extend(obj)

    def set_bg_img(self, bg_img):
        self.bg_img = bg_img

    def render(self, screen):
        for obj in self.objects:
            obj.render(screen)
        screen.blit(self.bg_img, (0, 0))


class StartRoom(Room):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load("data/start_room/bg_image.jpg")
        bg_img = pygame.transform.scale(bg_img, (800, 600))
        self.set_bg_img(bg_img)