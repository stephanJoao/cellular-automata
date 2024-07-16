import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_grid(grid_inicial, steps):
    grid_array = [grid_inicial]
    
    for step in range(steps-1):
        grid = grid_array[-1]
        for i in range(grid_size):
            for j in range(grid_size):
                left_neighbor_j = j - 1 if j > 0 else grid_size - 1
                right_neighbor_j = j + 1 if j < grid_size - 1 else 0
                up_neighbor_i = i - 1 if i > 0 else grid_size - 1
                down_neighbor_i = i + 1 if i < grid_size - 1 else 0

                neighbors_sum = (grid[up_neighbor_i][left_neighbor_j] + 
                                 grid[up_neighbor_i][j] + 
                                 grid[up_neighbor_i][right_neighbor_j] + 
                                 grid[i][left_neighbor_j] + 
                                 grid[i][right_neighbor_j] + 
                                 grid[down_neighbor_i][left_neighbor_j] + 
                                 grid[down_neighbor_i][j] + 
                                 grid[down_neighbor_i][right_neighbor_j])
                
                if grid[i][j] == 1:
                    if neighbors_sum < 2 or neighbors_sum > 3:
                        grid[i][j] = 0
                else:
                    if neighbors_sum == 3:
                        grid[i][j] = 1

        grid_array.append(grid)
        
    return np.array(grid_array)

def plot(grid_array, interval=20):
    # create an animation of the grid_array printing a grid that changes every interval
    fig, ax = plt.subplots()
    grid = grid_array[0]
    img = ax.imshow(grid, cmap='Greys')
    def animate(i):
        img.set_data(grid_array[i])
        return (img,)
    ani = animation.FuncAnimation(fig, animate, frames=len(grid_array), interval=interval, blit=True)
    plt.show()



# define grade inicial
grid_size = 20
steps = 100

initial_grid = [[0 for i in range(grid_size)] for j in range(grid_size)]
initial_grid[5][3] = 1
initial_grid[5][4] = 1
grid_array = []


update_grid(initial_grid, steps)
plot(initial_grid)
