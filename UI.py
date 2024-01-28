import pygame


# основной класс виджетов
class Widget:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.border_color = pygame.Color("white")
        self.background_color = pygame.Color("black")

    # задаем вид
    def set_view(self, x, y):
        self.x = x
        self.y = y

    # отрисовываем
    def render(self, screen):
        pass


# класс панели
class Panel(Widget):
    def __init__(self):
        super().__init__()

        self.widgets = []

    def render(self, screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.background_color, rect)
        pygame.draw.rect(screen, self.border_color, rect, 2)

        for widget in self.widgets:
            widget.render(screen)

    def get_click(self, mouse_pos):
        widget = self.get_widget(mouse_pos)
        if widget:
            widget.on_click()

    def get_widget(self, mouse_pos):
        for el in self.widgets:
            widget = el.get_field()
            if (widget.x < mouse_pos[0] < widget.x + widget.width
                    and widget.y < mouse_pos[1] < widget.y + widget.height):
                return el
        return None

    def add_widget(self, *widget):
        self.widgets.extend(widget)


# классы кнопки
class Button(Widget):
    def __init__(self):
        super().__init__()

        self.click_action = None

    def render(self, screen):
        pass

    def set_click_action(self, action):
        self.click_action = action

    def on_click(self):
        if self.click_action:
            self.click_action()

    def get_field(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class BaseButton(Button):
    def __init__(self):
        super().__init__()

    def set_view(self, x, y, width, height, background_color, border_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_color = border_color
        self.background_color = background_color

    def render(self, screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.background_color, rect)
        pygame.draw.rect(screen, self.border_color, rect, 2)


# кнопка с картинкой
class BeautifulButton(Button):
    def __init__(self, img):
        super().__init__()

        self.button_image = img
        self.rect = self.button_image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

    def render(self, screen: pygame.surface.Surface):
        screen.blit(self.button_image, (self.x, self.y))


# класс текста
class Text:
    def __init__(self):
        self.x, self.y = 0, 0
        self.text_size = 0
        self.text = ""
        self.text_color = pygame.Color("black")
        self.font = pygame.font.Font(None, self.text_size)

    # задаем вид
    def set_view(self, x, y, text_size, text, text_color):
        self.x, self.y = x, y
        self.text_size = text_size
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, self.text_size)

    # отрисовываем
    def render(self, screen: pygame.Surface):
        surface = self.font.render(self.text, True, self.text_color)
        screen.blit(surface, (self.x, self.y))

    def get_field(self):
        return self.font.render(self.text, True, self.text_color).get_rect()


class HealthBar:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.health_color = (0, 0, 0)
        self.background_color = (0, 0, 0)
        self.start_hp = 0
        self.now_hp = 0

    def set_view(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def set_color(self, health_color, background_color):
        self.health_color = health_color
        self.background_color = background_color

    def render(self, screen):
        hp_rect = pygame.Rect(self.x, self.y, self.width * (self.now_hp / self.start_hp), self.height)
        background_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.background_color, background_rect)
        pygame.draw.rect(screen, self.health_color, hp_rect)

    def get_field(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
