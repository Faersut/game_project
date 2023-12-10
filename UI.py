import pygame


class Widget:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

    def set_view(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, screen):
        pass


class Panel(Widget):
    def __init__(self):
        super().__init__()

        self.widgets = []

        self.border_color = pygame.Color("white")
        self.background_color = pygame.Color("black")
        self.text_color = pygame.Color("white")

    def render(self, screen):
        for widget in self.widgets:
            widget.render(screen)

    def get_click(self, mouse_pos):
        widget = self.get_widget(mouse_pos)
        if widget:
            widget.on_click()

    def get_widget(self, mouse_pos):
        for widget in self.widgets:
            if (widget.x < mouse_pos[0] < widget.x + widget.width
                    and widget.y < mouse_pos[0] < widget.y + widget.height):
                return widget
        return None


class Button(Widget):
    def __init__(self):
        super().__init__()

        self.border_color = pygame.Color("white")
        self.background_color = pygame.Color("black")

    def render(self, screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.background_color, rect)
        pygame.draw.rect(screen, self.border_color, rect, 2)

    def on_click(self):
        pass


class Text:
    def __init__(self):
        self.x, self.y = 0, 0
        self.text_size = 0
        self.text = ""
        self.text_color = pygame.Color("black")
        self.font = pygame.font.Font(None, self.text_size)

    def set_view(self, x, y, text_size, text, text_color):
        self.x, self.y = x, y
        self.text_size = text_size
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, self.text_size)

    def render(self, screen: pygame.Surface):
        text = self.font.render(self.text, True, self.text_color)
        screen.blit(text, (self.x, self.y))
