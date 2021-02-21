import pygame


class Rect:
    def __init__(self, win, x, y, width_x, width_y, color):
        # Переменные
        self.win = win
        self.x = x
        self.y = y
        self.width_x = width_x
        self.width_y = width_y
        self.color = color
        # Переменные для отрисовки
        self.draw_text = False

    def draw(self):
        pygame.draw.rect(self.win, self.color, (self.x, self.y,
                                                self.width_x, self.width_y))
        if self.draw_text:
            font = pygame.font.SysFont("Arial Black", int(self.text_width))
            text = font.render(self.text, True, self.text_color)
            self.win.blit(text, (self.x + self.text_x, self.y + self.text_y))

    def set_text(self, text, color=(255, 255, 255), text_width=None, text_x=None, text_y=None):
        self.text = text
        self.draw_text = True
        self.text_color = color
        if text_width is None:
            self.text_width = self.width_y // 2
            while len(self.text) * (self.text_width // 1.25) > self.width_x:
                self.text_width -= 1
        else:
            self.text_width = text_width
        if text_x is None:
            self.text_x = (self.width_x - len(self.text) * (self.text_width // 1.5)) // 2
        else:
            self.text_x = text_x
        if text_y is None:
            self.text_y = (self.width_y - self.text_width) // 2
        else:
            self.text_y = text_y