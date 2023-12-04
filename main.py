import pygame


def main():
    pygame.init()

    size = 1250, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Название игры")

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()


if __name__ == "__main__":
    main()
