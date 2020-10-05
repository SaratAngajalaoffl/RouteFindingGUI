import pygame


class Touchable_Rect():

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface):
        r = pygame.Rect(self.x-self.width/2, self.y -
                        self.height/2, self.width, self.height)
        pygame.draw.rect(surface, self.color, r)

    def is_on(self, co_ords):
        if self.x - self.width/2 <= co_ords[0] <= self.x + self.width/2 and self.y - self.height/2 <= co_ords[1] <= self.y + self.height/2:
            return True

    def set_color(self, color):
        self.color = color
