import pygame
from UI import *
from observers import *


def main():
    QUIT = pygame.USEREVENT + 1

    pygame.init()

    size = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Название игры")
    # основной игровой цикл
    running = True
    # работаем с UI
    main_menu = MainMenu()
    main_menu.exit_btn.set_click_action(lambda: pygame.event.post(pygame.event.Event(QUIT)))

    window_observer = WindowObserver()
    window_observer.set_active_window(main_menu)
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                window_observer.active_window.get_click(event.pos)

        window_observer.render(screen)
        # обновляем экран
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
