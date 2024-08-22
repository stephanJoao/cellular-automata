import random
import copy
from util import plot, plot2D


def update_grid(
    grid_array, steps, grid_size, rule_binary, border_condition="copy"
):
    for step in range(1, steps):
        grid_array[step] = copy.deepcopy(grid_array[step - 1])
        for j in range(grid_size[1]):
            if border_condition == "copy":
                if j == 0 or j == grid_size[1] - 1:
                    grid_array[step][step][j] = grid_array[step][step - 1][j]
                else:
                    neighbors = [
                        grid_array[step][step - 1][(j - 1) % grid_size[1]],
                        grid_array[step][step - 1][j],
                        grid_array[step][step - 1][(j + 1) % grid_size[1]],
                    ]
            neighbors_decimal = (
                int(neighbors[0]) * 4
                + int(neighbors[1]) * 2
                + int(neighbors[2])
            )
            grid_array[step][step][j] = int(
                rule_binary[-1 - neighbors_decimal]
            )

    return grid_array


if __name__ == "__main__":
    # variables
    x = 100
    y = 99  # odd
    grid_size = [x, y]
    steps = x
    rule = random.randint(0, 255)

    # create grid_array
    grid_array = [
        [[0 for j in range(grid_size[1])] for i in range(grid_size[0])]
        for k in range(steps)
    ]
    grid_array[0][0][y // 2] = 1

    # convert rule to binary
    rule_binary = format(rule, "08b")

    update_grid(grid_array, steps, grid_size, rule_binary)
    plot2D(grid_array, interval=100, gif="output/elementary-cellular-automata")
