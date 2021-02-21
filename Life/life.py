from main import Rect

import copy
import pygame


class Life:
    def __init__(self, width, height, rows, cols, brush, win_color, board_color, life_color):
        # Переменные настройки
        self.win_color = win_color
        self.board_color = board_color
        self.life_color = life_color
        self.brush = brush
        # Создание экрана
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height))
        self.button_menu = Rect(self.win, 0, 0, self.width // 4, self.height // 20,
                                (255 - win_color[0], 255 - win_color[1], 255 - win_color[2]))
        self.button_menu.set_text(text="Меню", color=win_color)
        # переменые
        self.exit = False
        self.run = True
        self.rows = rows
        self.cols = cols
        self.life_width = (self.width - self.width % self.rows) // self.rows
        self.life_height = (self.height - self.height % self.cols - self.height // 20) // self.cols
        self.not_life_width = self.width % self.rows // 2
        self.not_life_height = self.height % self.cols // 2 + self.height // 20
        self.life = False
        self.paint = False
        self.paint_life = False
        self.cords = []
        self.board = []
        self.new_board = []
        # Запуск
        self.draw_board()
        self.game()

    def game(self):
        # Создание окна
        pygame.init()
        pygame.display.set_caption("Своя игра")
        clock = pygame.time.Clock()
        # Переменные
        fps_stop_life = 60
        fps = 10
        # Игровой цикл
        while self.run:
            # FPS
            if self.life:
                clock.tick(fps)
            else:
                clock.tick(fps_stop_life)
            # События
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
                    self.run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.paint = True
                        self.paint_life = True
                        self.get_click(*event.pos)
                    if event.button == 3:
                        self.paint = True
                        self.paint_life = False
                        self.get_click(*event.pos)
                    if event.button == 4:
                        fps += 1
                    if event.button == 5 and fps > 1:
                        fps -= 1
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 or event.button == 3:
                        self.paint = False
                        self.paint_life = False
                if event.type == pygame.MOUSEMOTION:
                    if self.paint:
                        self.get_click(*event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.life = not self.life
                        print(self.life)
                    if event.key == pygame.K_f:
                        print("FPS:", fps)
            # Процесс
            if self.life:
                self.draw_new_board()
            # Прорисовка элементов
            self.win.fill(self.win_color)
            self.draw()
            pygame.display.update()

    def draw_new_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 1:
                    if self.cout_lifes(i, j) != 2 and self.cout_lifes(i, j) != 3:
                        self.new_board[i][j] = -1
                    for i1 in range(-1, 2, 1):
                        for j1 in range(-1, 2, 1):
                            if (0 <= i + i1 <= self.rows - 1 and
                                    0 <= j + j1 <= self.cols - 1 and (i1 != 0 or j1 != 0)):
                                if self.board[i + i1][j + j1] != 1 and self.cout_lifes(i + i1, j + j1) == 3:
                                    self.new_board[i + i1][j + j1] = 1
                            else:
                                if i + i1 == -1:
                                    i2 = self.rows - 1
                                elif i + i1 == self.rows:
                                    i2 = 0
                                else:
                                    i2 = i + i1
                                if j + j1 == -1:
                                    j2 = self.cols - 1
                                elif j + j1 == self.cols:
                                    j2 = 0
                                else:
                                    j2 = j + j1
                                if self.board[i2][j2] != 1 and self.cout_lifes(i2, j2) == 3:
                                    self.new_board[i2][j2] = 1

    def draw_board(self):
        c1 = []
        for i in range(self.rows):
            for j in range(self.cols):
                self.cords.append([i * self.life_width + self.not_life_width,
                                   j * self.life_height + self.not_life_height, i, j])
                c1.append(-1)
            self.board.append(c1)
            c1 = []
        self.new_board = copy.deepcopy(self.board)

    def draw(self):
        self.button_menu.draw()
        self.board = copy.deepcopy(self.new_board)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == -1:
                    pygame.draw.rect(self.win, self.board_color, (i * self.life_width + self.not_life_width,
                                                                  j * self.life_height + self.not_life_height,
                                                                  self.life_width, self.life_height))
                else:
                    pygame.draw.rect(self.win, self.life_color, (i * self.life_width + self.not_life_width,
                                                                 j * self.life_height + self.not_life_height,
                                                                 self.life_width, self.life_height))

    def get_click(self, x, y):
        for elem in self.cords:
            if (self.button_menu.x <= x <= self.button_menu.x + self.button_menu.width_x and
                    self.button_menu.y <= y <= self.button_menu.y + self.button_menu.width_y):
                self.run = False
                return x, y
            if (elem[0] - 1 < x < elem[0] + self.life_width + 1 and
                    elem[1] - 1 < y < elem[1] + self.life_height + 1):
                if self.paint:
                    if self.paint_life:
                        for i in range(self.brush * -1 + 1, self.brush, 1):
                            for j in range(self.brush * -1 + 1, self.brush, 1):
                                if 0 <= elem[2] + i < self.rows and 0 <= elem[3] + j < self.cols:
                                    self.board[elem[2] + i][elem[3] + j] = 1
                                    self.new_board[elem[2] + i][elem[3] + j] = 1
                    else:
                        self.board[elem[2]][elem[3]] = -1
                        self.new_board[elem[2]][elem[3]] = -1
                else:
                    self.board[elem[2]][elem[3]] *= -1
                    self.new_board[elem[2]][elem[3]] *= -1
                return self.board[elem[2]][elem[3]]
        return None

    def cout_lifes(self, i, j):
        lifes = 0
        for i1 in range(-1, 2, 1):
            for j1 in range(-1, 2, 1):
                if 0 <= i + i1 <= self.rows - 1 and 0 <= j + j1 <= self.cols - 1:
                    if self.board[i + i1][j + j1] == 1 and (i1 != 0 or j1 != 0):
                        lifes += 1
                elif i1 != 0 or j1 != 0:
                    if i + i1 == -1:
                        i2 = self.rows - 1
                    elif i + i1 == self.rows:
                        i2 = 0
                    else:
                        i2 = i + i1
                    if j + j1 == -1:
                        j2 = self.cols - 1
                    elif j + j1 == self.cols:
                        j2 = 0
                    else:
                        j2 = j + j1
                    if self.board[i2][j2] == 1:
                        lifes += 1
        return lifes

    def get_exit(self):
        print(self.exit)
        return self.exit
