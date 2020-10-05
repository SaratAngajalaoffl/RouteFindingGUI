import pygame
from .locals import *


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = None

    def set_color(self, color):
        self.color = color

    def draw(self, surface):
        if self.color:
            rect = pygame.Rect(GRIDX+self.x*ROW_WIDTH+1, GRIDY +
                               self.y*ROW_WIDTH+1, ROW_WIDTH-1, ROW_WIDTH-1)
            pygame.draw.rect(surface, self.color, rect)
