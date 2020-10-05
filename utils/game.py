import pygame
from .screens import *


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
                if self.screen == 1:
                    res = self.main_screen.check_clicks(pygame.mouse.get_pos())
                    if res == 0:
                        self.screen = 0
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
            self.draw()
            run = self.handle_events()
            pygame.display.update()
        pygame.quit()
