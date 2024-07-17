import matplotlib.pyplot as plt
import matplotlib.animation as animation

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