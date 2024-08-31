import pygame
import numpy as np
import matplotlib.pyplot as plt


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


def plot_results(grid_history):
    num_trees = np.array([np.sum(grid == 1) for grid in grid_history])
    num_fires = np.array([np.sum(grid == 2) for grid in grid_history])

    plt.plot(num_trees, label="Trees", color="green")
    plt.plot(num_fires, label="Fires", color="red")
    plt.xlim(0, 250)
    plt.ylim(0, 45000)
    plt.xlabel("Time")
    plt.ylabel("Número de células")
    plt.legend()
    plt.savefig("fire-spread.pdf")


def plot_results2(grid_history1, grid_history2):
    num_trees1 = np.array([np.sum(grid == 1) for grid in grid_history1])
    num_trees2 = np.array([np.sum(grid == 1) for grid in grid_history2])

    plt.plot(num_trees1, label="Árvores", color="green")
    plt.plot(
        num_trees2,
        label="Árvores Sem Barreira",
        color="green",
        linestyle="dashed",
    )
    plt.xlim(0, np.max([grid_history1.shape[0], grid_history2.shape[0]]))
    plt.ylim(0, np.max([np.max(num_trees1[0]), np.max(num_trees2[0])]) * 1.1)
    plt.xlabel("Tempo")
    plt.ylabel("Número de células")
    plt.legend()
    plt.grid()
    plt.savefig("fire-spread.pdf")


def animation_saved(grid_history, color_dict, cell_size=5, fps=30):
    # setup
    pygame.init()
    screen = pygame.display.set_mode(
        (len(grid_history[0][0]) * cell_size, len(grid_history[0]) * cell_size)
    )
    clock = pygame.time.Clock()

    running = True
    index = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        draw_grid(screen, grid_history[index], cell_size, color_dict)
        pygame.display.flip()
        clock.tick(fps)
        index += 1
        if index == len(grid_history):
            index = 0

    print("Animation saved")
    pygame.quit()


def animation(
    initial_grid,
    rule,
    color_dict,
    cell_size=5,
    fps=30,
    with_history=False,
    with_return=False,
):
    # setup
    pygame.init()
    screen = pygame.display.set_mode(
        (len(initial_grid[0]) * cell_size, len(initial_grid) * cell_size)
    )
    clock = pygame.time.Clock()
    grid = initial_grid

    history_saved = False
    if with_history:
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
            if with_history:
                grid_history = np.append(grid_history, [grid], axis=0)
                if (grid == old_grid).all():
                    history_saved = True
                    if with_return:
                        animation_saved(
                            grid_history, color_dict, cell_size, fps
                        )
                        return grid_history

    pygame.quit()
