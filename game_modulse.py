from main import *
import sqlite3
from rooms import *
import observers

QUIT = pygame.USEREVENT + 1
START_GAME = pygame.USEREVENT + 2


class MainMenuModule(Panel):
    def __init__(self):
        super().__init__()

        self.main_window_text = Text()
        self.main_window_text.set_view(150, 50, 40, "Главное меню", (0, 179, 255))
        self.game_btn = BaseButton()
        self.game_btn.set_view(160, 210, 180, 50, (0, 179, 255), (255, 255, 255))
        self.game_btn.set_click_action(lambda: pygame.event.post(pygame.event.Event(START_GAME)))
        self.game_text = Text()
        self.game_text.set_view(215, 225, 30, "Играть", (255, 255, 255))
        self.settings_btn = BaseButton()
        self.settings_btn.set_view(160, 300, 180, 50, (0, 179, 255), (255, 255, 255))
        self.settings_text = Text()
        self.settings_text.set_view(199, 315, 30, "Настройки", (255, 255, 255))
        self.exit_btn = BaseButton()
        self.exit_btn.set_view(160, 390, 180, 50, (0, 179, 255), (255, 255, 255))
        self.exit_btn.set_click_action(lambda: pygame.event.post(pygame.event.Event(QUIT)))
        self.exit_text = Text()
        self.exit_text.set_view(215, 405, 30, "Выход", (255, 255, 255))

        self.add_widget(self.main_window_text,
                        self.game_btn, self.game_text,
                        self.settings_btn, self.settings_text,
                        self.exit_btn, self.exit_text)


class CharacterTest(Panel):
    def __init__(self):
        super().__init__()

        self.QUESTIONS = [
            {
                "question": "Какой ваш любимый цвет?",
                "options": ["Оранжевый", "Синий", "Черный", "Розовый"]
            },
            {
                "question": "Какую суперсилу вы бы хотели иметь?",
                "options": ["Суперскорость", "Суперскрытность", "Магические чары", "Оживлять предметы"]
            },
            {
                "question": "Вам важно за кого вы будете играть?",
                "options": ["Нет", "Да, конечно"]
            }
        ]

        self.question_index = 0
        self.response_score = []
        self.i = 0

        self.question_text = Text()
        self.question_text.set_view(250, 100, 36,
                                    self.QUESTIONS[self.question_index]["question"], (255, 255, 255))

        for i, option_text in enumerate(self.QUESTIONS[self.question_index]["options"]):
            self.i = i
            btn_option = BaseButton()
            btn_option.set_view(300, 200 + i * 70, 250, 60, (0, 0, 0), (255, 255, 255))
            btn_option.set_click_action(self.option_action)
            btn_option_text = Text()
            btn_option_text.set_view(320, 220 + i * 70, 30, option_text, (255, 255, 255))
            self.add_widget(btn_option, btn_option_text)

        self.add_widget(self.question_text)

    def option_action(self):
        self.widgets = []
        self.question_index += 1
        if self.question_index < len(self.QUESTIONS):
            self.response_score.append(self.i)

            self.question_text.set_view(250, 100, 36,
                                        self.QUESTIONS[self.question_index]["question"], (255, 255, 255))
            for i, option_text in enumerate(self.QUESTIONS[self.question_index]["options"]):
                self.i = i
                btn_option = BaseButton()
                btn_option.set_view(300, 200 + i * 70, 250, 60, (0, 0, 0), (255, 255, 255))
                btn_option.set_click_action(self.option_action)
                btn_option_text = Text()
                btn_option_text.set_view(320, 220 + i * 70, 30, option_text, (255, 255, 255))
                self.add_widget(btn_option, btn_option_text)

            self.add_widget(self.question_text)
        else:
            res_text = self.result_test()
            res_text_wd = Text()
            res_text_wd.set_view(250, 300, 40, "Итог: " + res_text, (255, 255, 255))
            start_game_btn = BaseButton()
            start_game_btn.set_view(315, 450, 160, 50, (0, 0, 0), (255, 255, 255))
            start_game_btn.set_click_action(lambda: pygame.event.post(pygame.event.Event(START_GAME)))
            start_game_text = Text()
            start_game_text.set_view(325, 460, 35, "Начать игру", (255, 255, 255))
            self.add_widget(res_text_wd, start_game_btn, start_game_text)

    def result_test(self):
        total_score = sum(self.response_score)
        result = ""
        if total_score < 5:
            result = "Вы - светлый маг"
        elif 5 <= total_score < 10:
            result = "Вы - серый маг"
        elif total_score >= 10:
            result = "Вы - черный маг"

        connect = sqlite3.connect("player_data.db")
        cursor = connect.cursor()

        connect.execute("""
        CREATE TABLE IF NOT EXISTS PlayerData (
        id INTEGER PRIMARY KEY,
        hp INTEGER NOT NULL, 
        skin TEXT NOT NULL,
        inventory TEXT NOT NULL)""")
        connect.execute("""
        INSERT INTO PlayerData (hp, skin, inventory)
        VALUES (?, ?, ?)""", (0, result[5:], ""))

        connect.commit()
        connect.close()

        return result


class Game(Panel):
    def __init__(self):
        super().__init__()

        self.active_room = StartRoom()
        self.player = Player()
        self.enemy = None

        connect = sqlite3.connect("player_data.db")
        cursor = connect.cursor()

        cursor.execute("""
        SELECT skin FROM PlayerData""")
        skin = cursor.fetchall()

        if skin[0][0] == "серый маг":
            self.player.set_skins("data/skins/gray_mage_right.png",
                                  "data/skins/gray_mage_left.png")
            self.player.set_base_img("data/skins/gray_mage_right.png")
        elif skin[0][0] == "светлый маг":
            self.player.set_skins("data/skins/light_mage_right.png",
                                  "data/skins/light_mage_left.png")
            self.player.set_base_img("data/skins/light_mage_right.png")
        elif skin[0][0] == "черный маг":
            self.player.set_skins("data/skins/black_mage_right.png",
                                  "data/skins/black_mage_left.png")
            self.player.set_base_img("data/skins/black_mage_right.png")

        self.player.set_size(20, 30)
        self.player.rect.center = (self.player.rect.width // 2, self.player.rect.height // 2)
        self.player.set_pos(350, 250)

    def render(self, screen):
        self.active_room.render(screen)
        if isinstance(self.active_room, Arena1) or isinstance(self.active_room, Arena2):
            self.enemy.render(screen)
        self.player.render(screen)

    def update(self, event):
        self.player.update(event, self.active_room.rects, self.active_room, self.enemy)

        if event.type == GO_DANGEON:
            self.active_room = Dangeon()
            self.player.set_pos(400, 120)
        if event.type == EXIT_DANGEON:
            self.active_room = StartRoom()
            self.player.set_pos(350, 450)
        if event.type == FIRST_ARENA:
            self.active_room = Arena1()
            self.enemy = Skeleton()
            self.enemy.arena_active = True
        if event.type == SECOND_ARENA:
            self.active_room = Arena2()

    def enemy_update(self):
        if isinstance(self.active_room, Arena1) or isinstance(self.active_room, Arena2):
            self.enemy.update()