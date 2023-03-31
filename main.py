import pygame
import particle_processing

SELECTED_PARTICLE = 'sand'

FPS = 120
WIDTH = 1300
HEIGTH = 650

BRUSH_SIZE = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGTH))
MENU_BG = pygame.image.load("gfx/menu_screen.png").convert()
SAND_TEXT = pygame.image.load("gfx/sand_text.png").convert()
WATER_TEXT = pygame.image.load("gfx/water_text.png").convert()
BRICK_TEXT = pygame.image.load("gfx/brick_text.png").convert()
sand = pygame.image.load("gfx/sand.png").convert()
brick = pygame.image.load("gfx/brick.png").convert()
water = pygame.image.load("gfx/water.png").convert()

BUTTON_HIGHLIGHT = pygame.image.load("gfx/highlight.png").convert()
BUTTON_HIGHLIGHT.set_alpha(100)


def draw_buttons(click):
    global SELECTED_PARTICLE

    if SELECTED_PARTICLE == 'sand':
        WINDOW.blit(BUTTON_HIGHLIGHT, (1182, 1))
    elif SELECTED_PARTICLE == 'water':
        WINDOW.blit(BUTTON_HIGHLIGHT, (1242, 1))
    elif SELECTED_PARTICLE == 'brick':
        WINDOW.blit(BUTTON_HIGHLIGHT, (1182, 1 + 60))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x < 1180 and mouse_y > 240:
        return

    button_size = 60

    if 1182 < mouse_x < 1182 + button_size and 1 < mouse_y < 1 + button_size:
        WINDOW.blit(SAND_TEXT, (1061, 1))
        if click:
            SELECTED_PARTICLE = 'sand'

    elif 1242 < mouse_x < 1242 + button_size + button_size and 1 < mouse_y < 1 + button_size:
        WINDOW.blit(WATER_TEXT, (1061, 1))
        if click:
            SELECTED_PARTICLE = 'water'

    elif 1182 < mouse_x < 1182 + button_size and 1 + button_size < mouse_y < 1 + button_size*2:
        WINDOW.blit(BRICK_TEXT, (1061, 1))
        if click:
            SELECTED_PARTICLE = 'brick'


def add_particles(MAP, SELECTED_PARTICLE):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x > 1180 and mouse_y < 240:
        return
    mouse_x //= 5
    mouse_y //= 5
    element_to_draw = 0

    if SELECTED_PARTICLE == 'sand':
        element_to_draw = 1
    elif SELECTED_PARTICLE == 'water':
        element_to_draw = 2
    elif SELECTED_PARTICLE == 'brick':
        element_to_draw = 3

    for x in range(mouse_x - BRUSH_SIZE // 2, mouse_x + BRUSH_SIZE//2 + 1):
        for y in range(mouse_y- BRUSH_SIZE // 2, mouse_y + BRUSH_SIZE//2 + 1):
            try:
                MAP[y][x] = element_to_draw
            except IndexError:
                continue


def main():
    clock = pygame.time.Clock()
    PIXEL_MAP = [[0 for _ in range(260)] for _ in range(130)]
    DRAWING_POSITIONS = [[0 for _ in range(260)] for _ in range(130)]

    PIXEL_MAP[129] = [10 for _ in range(260)]
    for y, line in enumerate(DRAWING_POSITIONS):
        for x, particle in enumerate(line):
            DRAWING_POSITIONS[y][x] = (x*5, y*5)

    pygame.event.set_allowed((pygame.QUIT))

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        click = pygame.mouse.get_pressed()[0]

        particle_processing.process_whole_map(PIXEL_MAP, DRAWING_POSITIONS)
        WINDOW.blit(MENU_BG, (1180, 0))
        draw_buttons(click)
        if click:
            add_particles(PIXEL_MAP, SELECTED_PARTICLE)

        pygame.display.update()


if __name__ == "__main__":
    main()