import pygame
from .locals import *
from .button import Button
from .text import Text


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


class FinalScreen:
    pass
