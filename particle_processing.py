import pygame
from copy import deepcopy


def process_whole_map(map, drawing_positions):
    from main import WINDOW, sand, brick, water

    draw_to = pygame.Surface((1300, 650))
    for y, line in zip(range(129, 0, -1), reversed(map)):

        for x, particle in enumerate(line):
            if not particle:
                continue
            if y >= 129 or x >= 259 or x <= 0:
                continue

            if particle == 1:  # Sand
                draw_to.blit(sand, drawing_positions[y][x])

                if map[y + 1][x] == 0:
                    map[y][x] = 0
                    map[y + 1][x] = 1

                elif map[y + 1][x] == 2:
                    map[y][x] = 2
                    map[y + 1][x] = 1

                elif map[y + 1][x + 1] == 0:
                    map[y][x] = 0
                    map[y + 1][x + 1] = 1

                elif map[y + 1][x - 1] == 0:
                    map[y][x] = 0
                    map[y + 1][x - 1] = 1

            elif particle == 2:  # Water
                draw_to.blit(water, drawing_positions[y][x])

                if map[y + 1][x] == 0:
                    map[y][x] = 0
                    map[y + 1][x] = 2

                elif map[y + 1][x + 1] == 0:
                    map[y][x] = 0
                    map[y + 1][x + 1] = 2

                elif map[y + 1][x - 1] == 0:
                    map[y][x] = 0
                    map[y + 1][x - 1] = 2

                elif map[y][x + 1] == 0:
                    map[y][x] = 0
                    map[y][x + 1] = 2

                elif map[y][x - 1] == 0:
                    map[y][x] = 0
                    map[y][x - 1] = 2

            elif particle == 3:  # Brick
                draw_to.blit(brick, drawing_positions[y][x])

    WINDOW.blit(draw_to, (0, 0))

