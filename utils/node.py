import pygame
from .locals import *


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = None
        self.neighbors = []

    def get_color(self):
        return self.color

    def get_neighbors(self):
        return self.neighbors

    def update_neighbors(self, nodes):
        if self.y > 0 and nodes[self.y-1][self.x].get_color() != RED:
            self.neighbors.append(nodes[self.y-1][self.x])
        if self.y < ROWS-1 and nodes[self.y+1][self.x].get_color() != RED:
            self.neighbors.append(nodes[self.y+1][self.x])
        if self.x > 0 and nodes[self.y][self.x-1].get_color() != RED:
            self.neighbors.append(nodes[self.y][self.x-1])
        if self.x < ROWS-1 and nodes[self.y][self.x+1].get_color() != RED:
            self.neighbors.append(nodes[self.y][self.x+1])

    def __str__(self):
        return str(self.get_pos())

    def get_row(self):
        return self.y

    def get_col(self):
        return self.x

    def get_pos(self):
        return self.x, self.y

    def reset_color(self):
        self.color = None

    def set_color(self, color):
        if not (self.color and color != (0, 0, 0)):
            self.color = color

    def make_open(self):
        self.color = SKY_BLUE

    def make_closed(self):
        if self.color != PURPLE:
            self.color = LIGHT_YELLOW

    def make_path(self):
        self.color = PURPLE

    def draw(self, surface):
        if self.color:
            rect = pygame.Rect(GRIDX+self.x*ROW_WIDTH+1, GRIDY +
                               self.y*ROW_WIDTH+1, ROW_WIDTH-1, ROW_WIDTH-1)
            pygame.draw.rect(surface, self.color, rect)
