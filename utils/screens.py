import pygame
from .locals import *
from .button import Button
from .text import Text
from .node import Node


class MenuScreen:

    def __init__(self):
        self.options = [Button(RES/2, 4*RES/10, RES/3, RES/20,
                               WHITE, BLACK, 'freesansbold.ttf', 15, "A* ALGORITHM"), Button(RES/2, 5*RES/10, RES/3, RES/20,
                                                                                             WHITE, BLACK, 'freesansbold.ttf', 15, "DIJKSTRA ALGORITHM"), Button(RES/2, 6*RES/10, RES/3, RES/20,
                                                                                                                                                                 WHITE, BLACK, 'freesansbold.ttf', 15, "PRIMS ALGORITHM")]
        self.header = Text(RES/2, RES/10, RES/3, RES/10,
                           WHITE, 'freesansbold.ttf', 30, "SELECT ALGORITHM")
        self.start = Button(RES/2, 8*RES/10, RES/3, RES/20,
                            WHITE, BLACK, 'freesansbold.ttf', 15, "START")
        self.selected = None

    def draw(self, surface):
        for option in self.options:
            option.draw(surface)
        self.header.draw(surface)
        self.start.draw(surface)

    def check_selection_clicks(self, co_ords):
        for option in self.options:
            if option.is_on(co_ords):
                for i in self.options:
                    i.update_bg_color(WHITE)
                option.update_bg_color(BLUE)
                self.selected = option.get_text()

    def check_start_click(self, co_ords):
        if self.start.is_on(co_ords):
            return True

    def get_selected(self):
        return self.selected


class MainScreen:

    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.header = Text(RES/2, RES/10, RES/3, RES/10,
                           WHITE, 'freesansbold.ttf', 30, algorithm)
        self.menu_button = Button(3*RES/5, 9*RES/10, RES/6, RES/20,
                                  WHITE, BLACK, 'freesansbold.ttf', 15, "MENU")
        self.start_button = Button(2*RES/5, 9*RES/10, RES/6, RES/20,
                                   WHITE, BLACK, 'freesansbold.ttf', 15, "START")
        self.nodes = [[Node(i, j) for i in range(ROWS)]
                      for j in range(ROWS)]

    def draw_grid(self, surface):
        for i in range(0, ROWS+1):
            pygame.draw.line(surface, WHITE, (GRIDX+i*ROW_WIDTH, GRIDY),
                             (GRIDX+i*ROW_WIDTH, GRIDY+GRID_WIDTH))
            pygame.draw.line(surface, WHITE, (GRIDX, GRIDY+i*ROW_WIDTH),
                             (GRIDX+GRID_WIDTH, GRIDY+i*ROW_WIDTH))

    def check_clicks(self, co_ords, click="LEFT"):
        if self.menu_button.is_on(co_ords):
            return 0
        elif self.start_button.is_on(co_ords):
            return 0
        elif GRIDX <= co_ords[0] <= GRIDX + GRID_WIDTH and GRIDY <= co_ords[1] <= GRIDY + GRID_WIDTH:
            row = int((co_ords[0]-GRIDX) / ROW_WIDTH)
            col = int((co_ords[1]-GRIDY) / ROW_WIDTH)
            if click == "LEFT":
                self.nodes[col][row].set_color(RED)
            else:
                self.nodes[col][row].set_color(BLACK)

    def draw(self, surface):
        self.header.draw(surface)
        self.menu_button.draw(surface)
        self.start_button.draw(surface)
        self.draw_grid(surface)
        for i in self.nodes:
            for j in i:
                j.draw(surface)


class FinalScreen:
    pass
