import pygame
from main import WINDOW

sand = pygame.image.load("gfx/sand.png")


class World:
    def __init__(self):
        self.PIXEL_MAP = [[0 for _ in range(260)] for _ in range(130)]
        self.DRAWING_POSITIONS = [[0 for _ in range(260)] for _ in range(130)]


class Empty:
    def __init__(self):
        self.id = 0


class Sand:
    def __init__(self):
        self.id = 1

    def update_pos(self, MAP, x, y):
        if MAP[y + 1][x] == 0:
            MAP[y][x] = 0
            MAP[y + 1][x] = 1
        elif MAP[y + 1][x + 1] == 0:
            MAP[y][x] = 0
            MAP[y + 1][x + 1] = 1
        elif MAP[y + 1][x - 1] == 0:
            MAP[y][x] = 0
            MAP[y + 1][x - 1] = 1

    def draw(self, xy):
        WINDOW.blit(sand, (xy[0], xy[1]))