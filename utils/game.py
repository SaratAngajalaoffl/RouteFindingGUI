import pygame
from .screens import *
import threading


class Game:

    def __init__(self, bg, size, framerate=120):
        pygame.init()
        self.WIN = pygame.display.set_mode((size, size))
        pygame.display.set_caption("ALGO VISUALISER")
        self.bg = bg
        self.screen = 0
        self.framerate = framerate
        self.clock = pygame.time.Clock()
        self.menu_screen = MenuScreen()
        self.main_screen = None
        self.final_screen = None

    def draw(self):
        self.WIN.fill(self.bg)
        if self.screen == 0:
            self.menu_screen.draw(self.WIN)
        elif self.screen == 1:
            self.main_screen.draw(self.WIN)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if pygame.mouse.get_pressed()[0]:
                if self.screen == 0:
                    self.menu_screen.check_selection_clicks(
                        pygame.mouse.get_pos())
                    if self.menu_screen.check_start_click(
                            pygame.mouse.get_pos()):
                        self.start_main(self.menu_screen.get_selected())
                        self.screen = 1
                elif self.screen == 1:
                    res = self.main_screen.check_clicks(pygame.mouse.get_pos())
                    if res == 0:
                        self.screen = 0
                    if res == 1:
                        self.screen = 2
                        if self.main_screen.run_algo(self.WIN):
                            self.main_screen.set_title("THERE EXISTS A PATH")
                        else:
                            self.main_screen.set_title("PATH NOT FOUND")
                        self.screen = 1
            elif pygame.mouse.get_pressed()[2]:
                if self.screen == 1:
                    res = self.main_screen.check_clicks(
                        pygame.mouse.get_pos(), "RIGHT")
                    if res == 0:
                        self.screen = 0
        return True

    def start_main(self, ALGORITHM):
        self.main_screen = MainScreen(ALGORITHM)

    def run(self):
        run = True
        while run:
            self.clock.tick(self.framerate)
            t1 = threading.Thread(self.draw())
            t1.start()
            run = self.handle_events()
            pygame.display.update()
        t1.join()
        pygame.quit()
