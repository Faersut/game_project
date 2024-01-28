import pygame

from game_modulse import *


class WindowObserver:
    def __init__(self):
        self.active_window = MainMenuModule()
        pygame.event.post(pygame.event.Event(MENU))

    def set_active_window(self, window):
        self.active_window = window

    def render(self, screen):
        self.active_window.render(screen)
