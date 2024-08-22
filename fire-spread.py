import random
from util import plot


def update_grid(grid_array, steps, grid_size, lightning_prob=0.01):
    for step in range(1, steps):
        for i in range(grid_size[0]):
            for j in range(grid_size[1]):

                if grid_array[step - 1][i][j] == BURNING:
                    grid_array[step][i][j] = EMPTY
                elif grid_array[step - 1][i][j] == TREE:

                    neighbors = []
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue
                            ni, nj = i + di, j + dj
                            if (
                                0 <= ni < grid_size[0]
                                and 0 <= nj < grid_size[1]
                            ):
                                neighbors.append(grid_array[step - 1][ni][nj])
                            else:
                                neighbors.append(EMPTY)

                    if (
                        BURNING in neighbors
                        or random.random() < lightning_prob
                    ):
                        grid_array[step][i][j] = BURNING
                    else:
                        grid_array[step][i][j] = TREE
                else:
                    grid_array[step][i][j] = grid_array[step - 1][i][j]

    return grid_array


if __name__ == "__main__":
    # variables
    EMPTY, TREE, BURNING = 0, 1, 2
    colors = {0: "white", 1: "green", 2: "red"}
    grid_size = [100, 100]
    steps = 100
    tree_density = 0.5
    initial_fire_count = 1
    lightning_prob = 0
    # other possibilities: diff tree densities, multiple tree types,
    # firebreaks (areas that can't burn), variable burn rates, wind, 
    # probabilistic spreads, topography, etc.

    # create grid_array
    grid_array = [
        [[0 for j in range(grid_size[1])] for i in range(grid_size[0])]
        for k in range(steps)
    ]

    # initialize with trees
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if random.random() < tree_density:
                grid_array[0][i][j] = TREE

    # start fires at random location
    for _ in range(initial_fire_count):
        x, y = random.randint(0, grid_size[0] - 1), random.randint(
            0, grid_size[1] - 1
        )
        grid_array[0][x][y] = BURNING

    update_grid(grid_array, steps, grid_size, lightning_prob)
    plot(grid_array, interval=100, gif="output/fire-spread", colors=colors)
