from main import Rect

import pygame
from pymsgbox import prompt, alert


class Settings:
    def __init__(self, width, height, rows, cols, brush, win_color, board_color, life_color):
        self.update(width, height, rows, cols, brush, win_color, board_color, life_color)

    def update(self, width=None, height=None, rows=None, cols=None, brush=None,
               win_color=None, board_color=None, life_color=None):
        self.exit = False
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        self.win = pygame.display.set_mode((self.width, self.height))
        widgets = 7
        coff_x = 2.5
        # Цвет экрана
        if win_color is not None:
            self.win_color = win_color
        self.anti_win_color = (255 - self.win_color[0], 255 - self.win_color[1], 255 - self.win_color[2])
        self.value_win_color = Rect(self.win, self.width // 100,
                                    self.height // widgets * 0 + self.height // 100,
                                    self.width // coff_x, self.height // widgets * 0.5, self.win_color)
        self.value_win_color.set_text("Red:{0}, Green:{1}, Blue:{2}".format(str(self.win_color[0]),
                                                                            str(self.win_color[1]),
                                                                            str(self.win_color[2])),
                                      color=self.anti_win_color)
        self.button_win_color = Rect(self.win, self.width // 100 + self.width // coff_x,
                                     self.height // widgets * 0 + self.height // 100,
                                     self.width // coff_x, self.height // widgets * 0.5, self.anti_win_color)
        self.button_win_color.set_text("Изменить цвет экрана", color=self.win_color)
        # Цвет игрового поля
        if board_color is not None:
            self.board_color = board_color
        self.value_board_color = Rect(self.win, self.width // 100,
                                      self.height // widgets * 1 + self.height // 100,
                                      self.width // coff_x, self.height // widgets * 0.5, self.win_color)
        self.value_board_color.set_text("Red:{0}, Green:{1}, Blue:{2}".format(str(self.board_color[0]),
                                                                              str(self.board_color[1]),
                                                                              str(self.board_color[2])),
                                        color=self.anti_win_color)
        self.button_board_color = Rect(self.win, self.width // 100 + self.width // coff_x,
                                       self.height // widgets * 1 + self.height // 100,
                                       self.width // coff_x, self.height // widgets * 0.5, self.anti_win_color)
        self.button_board_color.set_text("Изменить цвет игрового поля", color=self.win_color)
        # Цвет клеток
        if life_color is not None:
            self.life_color = life_color
        self.value_life_color = Rect(self.win, self.width // 100,
                                     self.height // widgets * 2 + self.height // 100,
                                     self.width // coff_x, self.height // widgets * 0.5, self.win_color)
        self.value_life_color.set_text("Red:{0}, Green:{1}, Blue:{2}".format(str(self.life_color[0]),
                                                                             str(self.life_color[1]),
                                                                             str(self.life_color[2])),
                                       color=self.anti_win_color)
        self.button_life_color = Rect(self.win, self.width // 100 + self.width // coff_x,
                                      self.height // widgets * 2 + self.height // 100,
                                      self.width // coff_x, self.height // widgets * 0.5, self.anti_win_color)
        self.button_life_color.set_text("Изменить цвет клеток", color=self.win_color)
        # кисть
        if brush is not None:
            self.brush = brush
        self.value_size_brush = Rect(self.win, self.width // 100,
                              self.height // widgets * 3 + self.height // 100,
                              self.width // coff_x, self.height // widgets * 0.5, self.win_color)
        self.value_size_brush.set_text(str(self.brush), color=self.anti_win_color)
        self.button_size_brush = Rect(self.win, self.width // 100 + self.width // coff_x,
                               self.height // widgets * 3 + self.height // 100,
                               self.width // coff_x, self.height // widgets * 0.5, self.anti_win_color)
        self.button_size_brush.set_text("Размер кисти", color=self.win_color)
        # Размеры игрового поля
        if rows is not None:
            self.rows = rows
        if cols is not None:
            self.cols = cols
        self.value_board_size = Rect(self.win, self.width // 100,
                                     self.height // widgets * 4 + self.height // 100,
                                     self.width // coff_x, self.height // widgets * 0.5, self.win_color)
        self.value_board_size.set_text(str(self.rows) + "x" + str(self.cols),
                                       color=self.anti_win_color)
        self.button_board_size = Rect(self.win, self.width // 100 + self.width // coff_x,
                                      self.height // widgets * 4 + self.height // 100,
                                      self.width // coff_x, self.height // widgets * 0.5, self.anti_win_color)
        self.button_board_size.set_text("Изменить размеры игрового поля", color=self.win_color)
        # Размеры экрана
        self.value_size = Rect(self.win, self.width // 100,
                               self.height // widgets * 5 + self.height // 100,
                               self.width // coff_x, self.height // widgets * 0.5, self.win_color)
        self.value_size.set_text(str(self.width) + "x" + str(self.height),
                                 color=self.anti_win_color)
        self.button_size = Rect(self.win, self.width // 100 + self.width // coff_x,
                                self.height // widgets * 5 + self.height // 100,
                                self.width // coff_x, self.height // widgets * 0.5, self.anti_win_color)
        self.button_size.set_text("Изменить размеры экрана", color=self.win_color)
        # Кнопка "Ок"
        self.button_ok = Rect(self.win, self.width - self.width // 5,
                              self.height // widgets * 6 + self.height // 100,
                              self.width // 5, self.height // widgets * 0.5, self.anti_win_color)
        self.button_ok.set_text("Ок", color=self.win_color)
        self.game()

    def game(self):
        # Создание окна
        pygame.init()
        pygame.display.set_caption("Настройки")
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
                    self.exit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(self.get_click(*event.pos))

    def draw(self):
        # Цвет экрана
        self.value_win_color.draw()
        self.button_win_color.draw()
        # Цвет игрового поля
        self.value_board_color.draw()
        self.button_board_color.draw()
        # Цвет клеток
        self.value_life_color.draw()
        self.button_life_color.draw()
        # Бесконечная плоскость
        self.value_size_brush.draw()
        self.button_size_brush.draw()
        # Размеры игрового поля
        self.value_board_size.draw()
        self.button_board_size.draw()
        # Размеры экрана
        self.value_size.draw()
        self.button_size.draw()
        # Кнопка "Ок"
        self.button_ok.draw()

    def get_click(self, x, y):
        # Цвет экрана
        if (self.button_win_color.x < x < self.button_win_color.x + self.button_win_color.width_x and
                self.button_win_color.y < y < self.button_win_color.y + self.button_win_color.width_y):
            color = self.get_color()
            if color is not None:
                self.win_color = color
                self.update()
        # Цвет игрового поля
        elif (self.button_board_color.x < x < self.button_board_color.x + self.button_board_color.width_x and
              self.button_board_color.y < y < self.button_board_color.y + self.button_board_color.width_y):
            color = self.get_color()
            if color is not None:
                self.board_color = color
                self.update()
        # Цвет клеток
        elif (self.button_life_color.x < x < self.button_life_color.x + self.button_life_color.width_x and
              self.button_life_color.y < y < self.button_life_color.y + self.button_life_color.width_y):
            color = self.get_color()
            if color is not None:
                self.life_color = color
                self.update()
        # Размер кисти
        elif (self.button_size_brush.x < x < self.button_size_brush.x + self.button_size_brush.width_x and
              self.button_size_brush.y < y < self.button_size_brush.y + self.button_size_brush.width_y):
            boolean = True
            while boolean:
                try:
                    inp = int(prompt(text='Введите значение размера кисти(от 1 до 5)',
                                      title='Ввод'))
                    if not 1 <= inp <= 5:
                        alert(text='Введите численное значение от 1 до 5', title='Ошибка ввода')
                    else:
                        self.brush = inp
                        self.update()
                        boolean = False
                except ValueError:
                    alert(text='Введите численное значение от 1 до 5', title='Ошибка ввода')
                except TypeError:
                    boolean = False
        # Размеры игрового поля
        elif (self.button_board_size.x < x < self.button_board_size.x + self.button_board_size.width_x and
              self.button_board_size.y < y < self.button_board_size.y + self.button_board_size.width_y):
            boolean = True
            while boolean:
                try:
                    rows = int(prompt(text='Введите ширину игрового поля(по умолчанию 50)',
                                      title='Ввод'))
                    cols = int(prompt(text='Введите высоту игрового поля(по умолчанию 50)',
                                      title='Ввод'))
                    if (not 1 <= rows <= 200 and not 1 <= cols <= 200):
                        alert(text='Введите численное значение от 1 до 200', title='Ошибка ввода')
                    elif rows > self.width or cols > self.height:
                        alert(text='Размеры поля должны быть меньше размера экрана', title='Ошибка ввода')
                    else:
                        self.rows = rows
                        self.cols = cols
                        self.update()
                        boolean = False
                except ValueError:
                    alert(text='Введите численное значение от 1 до 200', title='Ошибка ввода')
                except TypeError:
                    boolean = False
        # Размеры экрана
        elif (self.button_size.x < x < self.button_size.x + self.button_size.width_x and
              self.button_size.y < y < self.button_size.y + self.button_size.width_y):
            boolean = True
            while boolean:
                try:
                    width = int(prompt(text='Введите высоту экрана(больше 100)',
                                       title='Ввод'))
                    height = int(prompt(text='Введите ширину экрана(больше 100)',
                                        title='Ввод'))
                    if width < 100 and height < 100:
                        alert(text='Введите численное значение больше 100', title='Ошибка ввода')
                    elif width < self.rows or height < self.cols:
                        alert(text='Размеры поля должны быть меньше размера экрана', title='Ошибка ввода')
                    else:
                        self.width = width
                        self.height = height
                        self.update()
                        boolean = False
                except ValueError:
                    alert(text='Введите численное значение от 1 до 200', title='Ошибка ввода')
                except TypeError:
                    boolean = False
        elif (self.button_ok.x < x < self.button_ok.x + self.button_ok.width_x and
              self.button_ok.y < y < self.button_ok.y + self.button_ok.width_y):
            self.run = False
        return x, y

    def update_menu(self):
        return (self.width, self.height, self.rows, self.cols, self.brush, self.win_color,
                self.board_color, self.life_color), self.exit

    def get_color(self):
        boolean = True
        while boolean:
            try:
                red = int(prompt(text='Введите значение Red (от 0 до 255)',
                                 title='Ввод'))
                green = int(prompt(text='Введите значение Green (от 0 до 255)',
                                   title='Ввод'))
                blue = int(prompt(text='Введите значение Blue (от 0 до 255)',
                                  title='Ввод'))
                if (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
                    boolean = False
                    color = (red, green, blue)
                    return color
                else:
                    alert(text='Введите численное значение от 0 до 255', title='Ошибка ввода')
            except ValueError:
                alert(text='Введите численное значение от 0 до 255', title='Ошибка ввода')
            except TypeError:
                boolean = False
