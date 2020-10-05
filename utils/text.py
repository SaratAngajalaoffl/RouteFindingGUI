import pygame


class Text():

    def __init__(self, x, y, width, height, color, font, fontsize, text):
        pygame.font.init()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.font = pygame.font.Font(font, fontsize)
        self.text = text
        self.textobj = self.font.render(text, True, color)
        self.text_rect = self.textobj.get_rect()
        self.text_rect.center = x, y

    def draw(self, surface):
        surface.blit(self.textobj, self.text_rect)

    def set_color(self, color):
        self.textobj = self.font.render(
            self.text, True, color)
        self.text_rect = self.textobj.get_rect()
        self.text_rect.center = self.x, self.y

    def get_text(self):
        return self.text
