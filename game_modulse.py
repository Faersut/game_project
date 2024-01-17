import pygame

import main
from UI import *
from main import *

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
            self.add_widget(res_text_wd)

    def result_test(self):
        total_score = sum(self.response_score)
        result = ""
        if total_score < 5:
            result = "Вы - светлый маг"
        elif 5 <= total_score < 10:
            result = "Вы - серый маг"
        elif total_score >= 10:
            result = "Вы - черный маг"

        return result
