import os.path

import pygame
from UI import *
from observers import *
from game_modulse import *
import sqlite3

completed_level = ("",)
if os.path.exists("player_data.db"):
    connect = sqlite3.connect("player_data.db")
    cursor = connect.cursor()

    cursor.execute("""
                    SELECT completed_level FROM PlayerData""")
    res = cursor.fetchall()
    for el in res:
        completed_level = el

    connect.close()


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
                    pygame.mixer.music.load("data/music/start_room_music.mp3")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.1)
            if isinstance(window_observer.active_window, Game):
                window_observer.active_window.update(event)
            if event.type == GAME_OVER:
                window_observer.set_active_window(GameOver())
            if event.type == WIN_FIRST_ENEMY:
                window_observer.set_active_window(WinFirstEnemy())
            if event.type == WIN_SECOND_ENEMY:
                window_observer.set_active_window(WinSecondEnemy())
            if event.type == MENU:
                window_observer.set_active_window(MainMenuModule())
                pygame.mixer.music.load("data/music/menu_music.mp3")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)

        if isinstance(window_observer.active_window, Game):
            window_observer.active_window.enemy_update()
        window_observer.render(screen)

        clock.tick(FPS)
        # обновляем экран
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
