import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap, BoundaryNorm

def plot(grid_array, interval=50, gif=None, colors=None):
    fig, ax = plt.subplots()
    fig.subplots_adjust(0, 0, 1, 1)
    ax.axis('off')
    
    if colors is None:
        colors = {0: 'white', 1: 'black'}  # default colors
    
    # create the colormap and normalization based on the colors dictionary
    values = sorted(colors.keys())
    color_list = [colors[val] for val in values]
    cmap = ListedColormap(color_list)
    norm = BoundaryNorm(values + [values[-1] + 1], cmap.N)
    
    grid = grid_array[0]
    img = ax.imshow(grid, cmap=cmap, norm=norm)
    
    def animate(i):
        img.set_data(grid_array[i])
        return (img,)
    
    ani = animation.FuncAnimation(fig, animate, frames=len(grid_array), interval=interval, blit=True)
    
    if gif is not None:
        print('Saving gif...')
        ani.save(gif + '.gif', writer='pillow', dpi=80)
        print('Gif saved.')
    
    plt.show()
