import pygame


class WindowObserver:
    def __init__(self):
        self.active_window = None

    def set_active_window(self, window):
        self.active_window = window

    def render(self, screen):
        self.active_window.render(screen)
