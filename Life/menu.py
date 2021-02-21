from life import Life
from main import Rect
from settings import Settings


import pygame


class Menu:
    def __init__(self, width, height, rows, cols, brush, win_color, board_color, life_color):
        # Переменные настройки
        self.win_color = win_color
        self.board_color = board_color
        self.life_color = life_color
        self.brush = brush
        self.rows = rows
        self.cols = cols
        # Переменные
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height))
        x = int(self.width // 8)
        y = int(self.height // 8)
        width_x = x * 6
        width_y = y * 2
        self.game_but = Rect(self.win, x, y, width_x, width_y, (98, 149, 156))
        self.settings_but = Rect(self.win, x, y + width_y + 5, width_x, width_y, (193, 146, 119))
        self.exit_but = Rect(self.win, x, y + width_y * 2 + 10, width_x, width_y, (227, 208, 185))
        self.game_but.set_text("Играть", color=(53, 11, 64))
        self.settings_but.set_text("Настройки", color=(255, 196, 120))
        self.exit_but.set_text("Выйти", color=(173, 108, 128))
        self.game()

    def game(self):
        # Создание окна
        pygame.init()
        pygame.display.set_caption("Меню")
        clock = pygame.time.Clock()
        # Переменные
        fps = 60
        # Игровой цикл
        self.run = True
        while self.run:
            # FPS
            clock.tick(fps)
            # События
            # Управление
            # Прорисовка элементов
            self.win.fill(self.win_color)
            self.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(self.get_click(*event.pos))

    def draw(self):
        self.game_but.draw()
        self.settings_but.draw()
        self.exit_but.draw()

    def get_click(self, x, y):
        if (self.game_but.x <= x <= self.game_but.x + self.game_but.width_x and
           self.game_but.y <= y <= self.game_but.y + self.game_but.width_y):
            self.run = False
            a = Life(self.width, self.height, self.rows, self.cols, self.brush,
                     self.win_color, self.board_color, self.life_color)
            exit = a.get_exit()
            if not exit:
                Menu(self.width, self.height, self.rows, self.cols, self.brush,
                     self.win_color, self.board_color, self.life_color)
        if (self.exit_but.x <= x <= self.exit_but.x + self.exit_but.width_x and
            self.exit_but.y <= y <= self.exit_but.y + self.exit_but.width_y):
            self.run = False
        if (self.settings_but.x <= x <= self.settings_but.x + self.settings_but.width_x and
            self.settings_but.y <= y <= self.settings_but.y + self.settings_but.width_y):
            self.run = False
            a = Settings(self.width, self.height, self.rows, self.cols, self.brush,
                         self.win_color, self.board_color, self.life_color)
            inputs, exit = a.update_menu()
            if not exit:
                Menu(*inputs)
        return x, y


if __name__ == "__main__":
    Menu(640, 640, 50, 50, 1, (120, 220, 120), (220, 220, 220), (35, 35, 35))
