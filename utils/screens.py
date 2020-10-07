import pygame
from .locals import *
from .button import Button
from .text import Text
from .node import Node
from queue import PriorityQueue
import sys


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
        self.curr_color = RED
        self.start = None
        self.end = None

    def draw_grid(self, surface):
        for i in range(0, ROWS+1):
            pygame.draw.line(surface, WHITE, (GRIDX+i*ROW_WIDTH, GRIDY),
                             (GRIDX+i*ROW_WIDTH, GRIDY+GRID_WIDTH))
            pygame.draw.line(surface, WHITE, (GRIDX, GRIDY+i*ROW_WIDTH),
                             (GRIDX+GRID_WIDTH, GRIDY+i*ROW_WIDTH))

    def update_neighbors(self):
        for i in self.nodes:
            for j in i:
                j.update_neighbors(self.nodes)

    def draw_path(self, path_set, current, surface):
        while current in path_set:
            current = path_set[current]
            current.make_path()
            self.draw_algo(surface)

    def Astar_Algorithm(self, surface):
        self.update_neighbors()
        count = 0
        start, end = self.start, self.end
        open_set = PriorityQueue()
        open_set.put(
            (0, count, start))
        path_set = {}
        g_score = {node: float("inf") for row in self.nodes for node in row}
        g_score[start] = 0
        f_score = {node: float("inf") for row in self.nodes for node in row}
        f_score[start] = self.get_h_score(start, end)

        open_set_hash = {start}

        while not open_set.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == end:
                self.draw_path(path_set, end, surface)
                return True

            for neighbor in current.get_neighbors():
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score[neighbor]:
                    path_set[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + \
                        self.get_h_score(neighbor, end)
                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((f_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)
                        if neighbor != end:
                            neighbor.make_open()
                        self.draw_algo(surface)

            if current != start:
                current.make_closed()
                self.draw_algo(surface)

        return False

    def draw_algo(self, surface):
        pygame.time.delay(DELAY)
        surface.fill(BLACK)
        self.draw(surface)
        pygame.display.update()

    def run_algo(self, surface):
        if self.start and self.end:
            if self.algorithm == "A* ALGORITHM":
                return self.Astar_Algorithm(surface)
        else:
            print("Start and end Not selected")
            pygame.quit()
            sys.exit()

    def get_h_score(self, node_1, node_2):
        return abs(node_1.get_row() - node_2.get_row()) + abs(node_1.get_col() - node_2.get_col())

    def check_clicks(self, co_ords, click="LEFT"):
        if self.menu_button.is_on(co_ords):
            return 0
        elif self.start_button.is_on(co_ords):
            return 1
        elif GRIDX <= co_ords[0] <= GRIDX + GRID_WIDTH and GRIDY <= co_ords[1] <= GRIDY + GRID_WIDTH:
            row = int((co_ords[0]-GRIDX) / ROW_WIDTH)
            col = int((co_ords[1]-GRIDY) / ROW_WIDTH)
            if click == "LEFT":
                if not self.start:
                    self.start = self.nodes[col][row]
                    self.nodes[col][row].set_color(BLUE)
                elif not self.end:
                    self.end = self.nodes[col][row]
                    self.nodes[col][row].set_color(GREEN)
                else:
                    self.nodes[col][row].set_color(RED)
            elif click == "RIGHT":
                self.nodes[col][row].reset_color()
                if self.start == self.nodes[col][row]:
                    self.start = None
                elif self.end == self.nodes[col][row]:
                    self.end = None

    def set_title(self, title):
        self.header = Text(RES/2, RES/10, RES/3, RES/10,
                           WHITE, 'freesansbold.ttf', 30, title)

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
