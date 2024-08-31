import random
import numpy as np
from animation import animation


def update_grid(grid):
    new_grid = grid.copy()

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == BURNING:
                new_grid[i][j] = EMPTY
            elif grid[i][j] == TREE:
                neighbors = []
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < grid.shape[0] and 0 <= nj < grid.shape[1]:
                            neighbors.append(grid[ni][nj])
                        else:
                            neighbors.append(EMPTY)
                if BURNING in neighbors:
                    new_grid[i][j] = BURNING
                else:
                    new_grid[i][j] = TREE
            else:
                new_grid[i][j] = grid[i][j]

    return new_grid


if __name__ == "__main__":
    # variables
    EMPTY, TREE, BURNING = 0, 1, 2
    color_dict = {
        0: (255, 255, 255),
        1: (0, 255, 0),
        2: (255, 0, 0),
    }
    grid_size = [500, 500]
    tree_density = 0.5

    

    # initial grid
    initial_grid = np.zeros(grid_size)

    # initialize trees
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if random.random() < tree_density:
                initial_grid[i][j] = TREE

    # initialize firebreaks
    firebreak_positions = [
        slice(grid_size[0] * 2 / 3, grid_size[0] * 2 / 3 + 2),
        slice(grid_size[0] * 1 / 3, grid_size[0] * 2 / 3),
    ]

    # set firebreaks
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if (
                firebreak_positions[0].start <= i < firebreak_positions[0].stop
                and firebreak_positions[1].start
                <= j
                < firebreak_positions[1].stop
            ):
                initial_grid[i][j] = EMPTY  # This region acts as a firebreak

    # start fires at center
    i = grid_size[0] // 2
    j = grid_size[1] // 2
    initial_grid[i][j] = BURNING

    # other possibilities: diff tree densities, multiple tree types,
    # firebreaks (areas that can't burn), variable burn rates, wind,
    # probabilistic spreads, topography, etc.
    # lightning_prob = 0
    # initial_random_fire_count = 0

    initial_grid = np.array(initial_grid)
    animation(initial_grid, update_grid, color_dict, cell_size=1, fps=60)
