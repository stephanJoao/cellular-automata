import random
import numpy as np
from util import animation


def update_grid(grid):
    new_grid = grid.copy()

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            neighbors_sum = (
                grid[(i - 1) % grid_size[0]][(j - 1) % grid_size[1]]
                + grid[(i - 1) % grid_size[0]][j]
                + grid[(i - 1) % grid_size[0]][(j + 1) % grid_size[1]]
                + grid[i][(j - 1) % grid_size[1]]
                + grid[i][(j + 1) % grid_size[1]]
                + grid[(i + 1) % grid_size[0]][(j - 1) % grid_size[1]]
                + grid[(i + 1) % grid_size[0]][j]
                + grid[(i + 1) % grid_size[0]][(j + 1) % grid_size[1]]
            )
            # conway's rule
            if grid[i][j] == 1:
                if neighbors_sum < 2 or neighbors_sum > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            else:
                if neighbors_sum == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0

    return new_grid


if __name__ == "__main__":

    color_dict = {
        0: (255, 255, 255),
        1: (0, 0, 0),
    }

    grid_size = [100, 100]

    initial_grid = np.zeros(grid_size)

    # initialize cells
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if random.random() < 0.5:
                initial_grid[i][j] = 1

    animation(
        initial_grid,
        update_grid,
        color_dict,
        cell_size=10,
    )

    # examples
    # glider
    # grid_array[0][5][3] = 1
    # grid_array[0][5][4] = 1
    # grid_array[0][5][5] = 1
    # grid_array[0][4][5] = 1
    # grid_array[0][3][4] = 1
    # gosper's glider gun
    # grid_array[0][1][5] = 1
    # grid_array[0][1][6] = 1
    # grid_array[0][2][5] = 1
    # grid_array[0][2][6] = 1
    # grid_array[0][11][5] = 1
    # grid_array[0][11][6] = 1
    # grid_array[0][11][7] = 1
    # grid_array[0][12][4] = 1
    # grid_array[0][12][8] = 1
    # grid_array[0][13][3] = 1
    # grid_array[0][13][9] = 1
    # grid_array[0][14][3] = 1
    # grid_array[0][14][9] = 1
    # grid_array[0][15][6] = 1
    # grid_array[0][16][4] = 1
    # grid_array[0][16][8] = 1
    # grid_array[0][17][5] = 1
    # grid_array[0][17][6] = 1
    # grid_array[0][17][7] = 1
    # grid_array[0][18][6] = 1
    # grid_array[0][21][3] = 1
    # grid_array[0][21][4] = 1
    # grid_array[0][21][5] = 1
    # grid_array[0][22][3] = 1
    # grid_array[0][22][4] = 1
    # grid_array[0][22][5] = 1
    # grid_array[0][23][2] = 1
    # grid_array[0][23][6] = 1
    # grid_array[0][25][1] = 1
    # grid_array[0][25][2] = 1
    # grid_array[0][25][6] = 1
    # grid_array[0][25][7] = 1
    # grid_array[0][35][3] = 1
    # grid_array[0][35][4] = 1
    # grid_array[0][36][3] = 1
    # grid_array[0][36][4] = 1
