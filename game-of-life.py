import random
from util import plot

def update_grid(grid_array, steps, grid_size):
    for step in range(1, steps):
        for i in range(grid_size[0]):
            for j in range(grid_size[1]):

                neighbors_sum = (
                    grid_array[step - 1][(i - 1) % grid_size[0]][(j - 1) % grid_size[1]] + 
                    grid_array[step - 1][(i - 1) % grid_size[0]][j] + 
                    grid_array[step - 1][(i - 1) % grid_size[0]][(j + 1) % grid_size[1]] + 
                    grid_array[step - 1][i][(j - 1) % grid_size[1]] + 
                    grid_array[step - 1][i][(j + 1) % grid_size[1]] + 
                    grid_array[step - 1][(i + 1) % grid_size[0]][(j - 1) % grid_size[1]] + 
                    grid_array[step - 1][(i + 1) % grid_size[0]][j] + 
                    grid_array[step - 1][(i + 1) % grid_size[0]][(j + 1) % grid_size[1]]
                )
                
				# conway's rule
                if grid_array[step - 1][i][j] == 1:
                    if neighbors_sum < 2 or neighbors_sum > 3:
                        grid_array[step][i][j] = 0
                    else:
                        grid_array[step][i][j] = 1
                else:
                    if neighbors_sum == 3:
                        grid_array[step][i][j] = 1
                    else:
                        grid_array[step][i][j] = 0
        
    return grid_array

if __name__ == '__main__':    
	# variables
    grid_size = [100, 100]
    steps = 1000

    # create grid_array
    grid_array = [[[random.choice([0, 1]) for j in range(grid_size[1])] for i in range(grid_size[0])] for k in range(steps)]

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

    update_grid(grid_array, steps, grid_size)
    plot(grid_array, interval=50, gif='output/game-of-life')