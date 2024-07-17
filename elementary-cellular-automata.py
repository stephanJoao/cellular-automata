import random, copy
from util import plot

def update_grid(grid_array, steps, grid_size, rule):
    for step in range(1, steps):
        grid_array[step] = copy.deepcopy(grid_array[step - 1])
        for j in range(grid_size[1]):
            if j == 0 or j == grid_size[1] - 1:
                grid_array[step][step][j] = grid_array[step][step - 1][j]
            else:
                neighbors = [grid_array[step][step - 1][j - 1], grid_array[step][step - 1][j], grid_array[step][step - 1][j + 1]]
                neighbors_decimal = int(neighbors[0]) * 4 + int(neighbors[1]) * 2 + int(neighbors[2])
                grid_array[step][step][j] = int(rule[-1 - neighbors_decimal])
          
    return grid_array

if __name__ == '__main__':
    # variables
    x = 100
    y = 99
    grid_size = [x, y]
    steps = x

    # create grid_array with size [steps][grid_size[0]][grid_size[1]]
    grid_array = [[[0 for j in range(grid_size[1])] for i in range(grid_size[0])] for k in range(steps)]
    grid_array[0][0][y // 2] = 1
    rule = random.randint(0, 255)
    
	# convert rule to binary
    rule_binary = format(rule, '08b')

    update_grid(grid_array, steps, grid_size, rule_binary)
    plot(grid_array)