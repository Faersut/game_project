import pygame


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

        # переварачиваем экран
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
