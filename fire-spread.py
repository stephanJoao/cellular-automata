import random
from animation import animation
import numpy as np


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
    grid_size = [300, 300]
    tree_density = 0.5
    initial_random_fire_count = 0
    lightning_prob = 0
    # other possibilities: diff tree densities, multiple tree types,
    # firebreaks (areas that can't burn), variable burn rates, wind,
    # probabilistic spreads, topography, etc.

    # initial grid
    initial_grid = np.zeros(grid_size)

    # initialize with trees considering different densities
    dense_area = [slice(20, 40), slice(20, 40)]  # Example of a denser area
    sparse_area = [slice(60, 80), slice(60, 80)]  # Example of a sparser area

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if (
                dense_area[0].start <= i < dense_area[0].stop
                and dense_area[1].start <= j < dense_area[1].stop
            ):
                density = 0.5  # Higher density
            elif (
                sparse_area[0].start <= i < sparse_area[0].stop
                and sparse_area[1].start <= j < sparse_area[1].stop
            ):
                density = 0.5  # Lower density
            else:
                density = 0.5  # Default density

            if random.random() < density:
                initial_grid[i][j] = TREE

    # initialize firebreaks
    firebreak_positions = [
        slice(grid_size[0] * 2 / 3, grid_size[0] * 2 / 3 + 2),
        slice(grid_size[0] * 1 / 3, grid_size[0] * 2 / 3),
    ]  # Example firebreaks

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

    # start random fires
    for _ in range(initial_random_fire_count):
        i = random.randint(0, grid_size[0] - 1)
        j = random.randint(0, grid_size[1] - 1)
        initial_grid[i][j] = BURNING

    initial_grid = np.array(initial_grid)
    animation(initial_grid, update_grid, color_dict, cell_size=3, fps=30)
