import pygame
import numpy as np


def draw_grid(screen, grid, cell_size, color_dict):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            color = color_dict[val]
            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(
                    j * cell_size, i * cell_size, cell_size, cell_size
                ),
            )


def animation(initial_grid, rule, color_dict, cell_size=5, fps=30):
    # setup
    pygame.init()
    screen = pygame.display.set_mode(
        (len(initial_grid[0]) * cell_size, len(initial_grid) * cell_size)
    )
    clock = pygame.time.Clock()
    grid = initial_grid

    history_saved = False
    index = 0
    grid_history = np.array([initial_grid])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        if history_saved:
            draw_grid(screen, grid_history[index], cell_size, color_dict)
            pygame.display.flip()
            clock.tick(fps)
            index += 1
            if index == len(grid_history):
                index = 0
        else:
            draw_grid(screen, grid, cell_size, color_dict)
            pygame.display.flip()
            clock.tick(fps)
            old_grid = grid
            grid = rule(grid)
            grid_history = np.append(grid_history, [grid], axis=0)
            if (grid == old_grid).all():
                history_saved = True

    pygame.quit()
