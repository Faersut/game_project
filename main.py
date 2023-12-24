import pygame
from UI import *


def main():
    pygame.init()

    size = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Название игры")
    # основной игровой цикл
    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # обновляем экран
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
