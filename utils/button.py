from .text import Text
from .touchable_rect import *


class Button:

    def __init__(self, x, y, width, height, color, text_color, font, fontsize, inner_text):
        self.bg = Touchable_Rect(
            x, y, width, height, color)
        self.text = Text(x, y, width, height, text_color,
                         font, fontsize, inner_text)

    def draw(self, surface):
        self.bg.draw(surface)
        self.text.draw(surface)

    def is_on(self, co_ords):
        return self.bg.is_on(co_ords)

    def update_bg_color(self, color):
        self.bg.set_color(color)

    def update_text_color(self, color):
        self.text.set_color(color)

    def get_text(self):
        return self.text.get_text()
