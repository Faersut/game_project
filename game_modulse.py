from UI import *

QUIT = pygame.USEREVENT + 1


class MainMenuModule(Panel):
    def __init__(self):
        super().__init__()

        self.is_active = True

        self.main_window_text = Text()
        self.main_window_text.set_view(150, 50, 40, "Главное меню", (0, 179, 255))
        self.game_btn = BaseButton()
        self.game_btn.set_view(160, 210, 180, 50, (0, 179, 255), (255, 255, 255))
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
