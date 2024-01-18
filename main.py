import os.path

import pygame
from UI import *
from observers import *
from game_modulse import *


def main():
    FPS = 30

    pygame.init()

    size = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Название игры")
    # работаем с UI
    window_observer = WindowObserver()

    # основной игровой цикл
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                window_observer.active_window.get_click(event.pos)
            if event.type == START_GAME:
                if not os.path.exists("player_data.db"):
                    window_observer.set_active_window(CharacterTest())
                else:
                    window_observer.set_active_window(Game())
            if isinstance(window_observer.active_window, Game):
                window_observer.active_window.update(event)

        window_observer.render(screen)

        clock.tick(FPS)
        # обновляем экран
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
