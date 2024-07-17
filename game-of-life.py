import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_grid(grid_array, steps, grid_size):
    for step in range(1, steps):
        for i in range(grid_size):
            for j in range(grid_size):

                neighbors_sum = (grid_array[step - 1][(i - 1) % grid_size][(j - 1) % grid_size] + 
                                 grid_array[step - 1][(i - 1) % grid_size][j] + 
                                 grid_array[step - 1][(i - 1) % grid_size][(j + 1) % grid_size] + 
                                 grid_array[step - 1][i][(j - 1) % grid_size] + 
                                 grid_array[step - 1][i][(j + 1) % grid_size] + 
                                 grid_array[step - 1][(i + 1) % grid_size][(j - 1) % grid_size] + 
                                 grid_array[step - 1][(i + 1) % grid_size][j] + 
                                 grid_array[step - 1][(i + 1) % grid_size][(j + 1) % grid_size])
                
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

def plot(grid_array, interval=80):
    fig, ax = plt.subplots()
    fig.subplots_adjust(0, 0, 1, 1)
    ax.axis('off')
    grid = grid_array[0]
    img = ax.imshow(grid, cmap='Greys')
    def animate(i):
        img.set_data(grid_array[i])
        return (img,)
    ani = animation.FuncAnimation(fig, animate, frames=len(grid_array), interval=interval, blit=True)
    plt.show()

if __name__ == '__main__':
    # variables
    grid_size = 100
    steps = 300

    # create grid_array with size [steps][grid_size][grid_size]
    grid_array = [[[random.choice([0, 1]) for i in range(grid_size)] for j in range(grid_size)] for k in range(steps)]

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
    plot(grid_array)