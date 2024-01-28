from game_object import *


class Room:
    def __init__(self):
        self.objects = []
        self.bg_img = None
        self.rects = []

    def add_objects(self, *obj):
        self.objects.extend(obj)
        for el in obj:
            self.rects.append(el.rect)

    def set_bg_img(self, bg_img):
        self.bg_img = bg_img

    def render(self, screen):
        screen.blit(self.bg_img, (0, 0))
        for obj in self.objects:
            obj.render(screen)


class StartRoom(Room):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load("data/start_room/bg_image.jpg")
        bg_img = pygame.transform.scale(bg_img, (800, 600))
        self.set_bg_img(bg_img)

        self.stall = GameObject()
        self.stall.set_image("data/start_room/stall.jpg")
        self.stall.img = pygame.transform.scale(self.stall.img, (350, 220))
        self.stall.set_size(350, 220)

        self.plant_1 = GameObject()
        self.plant_1.set_image("data/start_room/plant.png")
        self.plant_1.img = pygame.transform.scale(self.plant_1.img, (100, 150))
        self.plant_1.set_pos(680, 150)
        self.plant_1.set_size(200, 150)
        self.plant_2 = GameObject()
        self.plant_2.set_image("data/start_room/plant.png")
        self.plant_2.img = pygame.transform.scale(self.plant_1.img, (100, 150))
        self.plant_2.set_pos(680, 350)
        self.plant_2.set_size(200, 150)

        self.picture = GameObject()
        self.picture.set_image("data/start_room/picture.png")
        self.picture.img = pygame.transform.scale(self.picture.img, (200, 120))
        self.picture.set_pos(450, 10)
        self.picture.set_size(400, 120)

        self.add_objects(self.stall,
                         self.plant_1, self.plant_2,
                         self.picture)


class Dangeon(Room):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load("data/dangeon_room/background_dungeon.png")
        bg_img = pygame.transform.scale(bg_img, (800, 600))
        self.set_bg_img(bg_img)

        self.back_wall = GameObject()
        self.back_wall.set_image("data/dangeon_room/back_wall.png")
        self.back_wall.set_size(800, 100)
        self.back_wall.set_pos(0, 0)

        self.exit = GameObject()
        self.exit.set_image("data/dangeon_room/exit.png")
        self.exit.set_size(100, 100)
        self.exit.set_pos(335, 15)

        self.entrace_arena_1 = GameObject()
        self.entrace_arena_1.set_image("data/dangeon_room/entrace_arena.png")
        self.entrace_arena_1.set_size(200, 100)
        self.entrace_arena_1.set_pos(100, 570)

        self.entrace_arena_2 = GameObject()
        self.entrace_arena_2.set_image("data/dangeon_room/entrace_arena.png")
        self.entrace_arena_2.set_size(200, 100)
        self.entrace_arena_2.set_pos(500, 570)

        self.add_objects(self.back_wall, self.exit,
                         self.entrace_arena_1, self.entrace_arena_2)


class Arena1(Room):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load("data/arena1/arena1_backgound.png")
        bg_img = pygame.transform.scale(bg_img, (800, 600))
        self.set_bg_img(bg_img)


class Arena2(Room):
    def __init__(self):
        super().__init__()