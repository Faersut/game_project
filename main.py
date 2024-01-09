import pygame
from UI import *
from observers import *
from game_modulse import *


def main():
    pygame.init()

    size = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Название игры")
    # работаем с UI
    test = CharacterTest()

    window_observer = WindowObserver()
    #window_observer.set_active_window(test)
    # основной игровой цикл
    running = True
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
