import random
import numpy as np
from util import animation, plot_results2


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

    EMPTY, TREE, BURNING = 0, 1, 2

    color_dict = {
        EMPTY: (255, 255, 255),
        TREE: (0, 255, 0),
        BURNING: (255, 0, 0),
    }

    grid_size = [300, 300]
    tree_density = 0.5

    # initial grid
    initial_grid = np.zeros(grid_size)

    # initialize trees
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if random.random() < tree_density:
                initial_grid[i][j] = TREE

    initial_grid_2 = initial_grid.copy()

    # initialize firebreaks
    firebreak_positions = [
        slice(grid_size[0] * 0.55, grid_size[0] * 0.55 + 2),
        slice(grid_size[0] * 0.2, grid_size[0] * 0.8),
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
                initial_grid_2[i][j] = EMPTY

    # start fires at center
    i = grid_size[0] // 2
    j = grid_size[1] // 2
    initial_grid[i][j] = BURNING
    initial_grid_2[i][j] = BURNING

    # history
    num_trees = np.array(np.sum(initial_grid == TREE))
    num_fires = np.array(np.sum(initial_grid == BURNING))

    grid_history_1 = animation(
        initial_grid,
        update_grid,
        color_dict,
        cell_size=3,
        fps=30,
        with_history=True,
        with_return=True,
    )
    grid_history_2 = animation(
        initial_grid_2,
        update_grid,
        color_dict,
        cell_size=3,
        fps=30,
        with_history=True,
        with_return=True,
    )
    plot_results2(grid_history_1, grid_history_2)
