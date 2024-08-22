import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np

import seaborn as sns


def plot(grid_array, interval=50, gif=None, colors=None):
    fig, ax = plt.subplots()
    fig.subplots_adjust(0, 0, 1, 1)
    ax.axis("off")

    if colors is None:
        colors = {0: "white", 1: "black"}  # default colors

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

    ani = animation.FuncAnimation(
        fig, animate, frames=len(grid_array), interval=interval, blit=True
    )

    if gif is not None:
        print("Saving gif...")
        ani.save(gif + ".gif", writer="pillow", dpi=80)
        print("Gif saved.")

    plt.show()

def plot2D(grid_array, interval=50, gif=None, colors=None):
    fig, ax = plt.subplots()
    ax.axis("off")

    # Set default colors if none provided
    if colors is None:
        colors = {1: "green", 2: "brown"}  # example colors for different types of terrain

    # Normalize grid values to color indices
    cmap = plt.cm.colors.ListedColormap([colors[val] for val in sorted(colors.keys())])
    bounds = sorted(colors.keys()) + [max(colors.keys()) + 1]
    norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

    def animate(i):
        ax.clear()
        ax.axis("off")
        Z = np.where(grid_array[i] == 0, np.nan, grid_array[i])
        c = ax.pcolormesh(Z, cmap=cmap, norm=norm, edgecolor='face')
        return c,

    ani = animation.FuncAnimation(
        fig, animate, frames=len(grid_array), interval=interval, blit=False
    )

    if gif is not None:
        print("Saving gif...")
        ani.save(gif + ".gif", writer="pillow", dpi=80)
        print("Gif saved.")

    plt.show()

def plot3D(grid_array, interval=50, gif=None, colors=None, bar_height=0.2):
    grid_array = np.array(grid_array)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    fig.subplots_adjust(0, 0, 1, 1)
    ax.axis("off")

    # Create a meshgrid for X and Y coordinates
    x = np.arange(grid_array[0].shape[1])
    y = np.arange(grid_array[0].shape[0])
    X, Y = np.meshgrid(x, y)
    X = X.ravel()
    Y = Y.ravel()

    # Set default colors if none provided
    if colors is None:
        colors = {1: "green", 2: "brown"}  # example colors for different types of terrain

    def get_color(val):
        return colors[val]

    def animate(i):
        ax.clear()
        ax.axis("off")

        Z = grid_array[i].ravel()
        non_zero_indices = np.where(Z != 0)

        X_non_zero = X[non_zero_indices]
        Y_non_zero = Y[non_zero_indices]
        Z_non_zero = Z[non_zero_indices]
        color = np.array([get_color(val) for val in Z_non_zero])

        ax.bar3d(X_non_zero, Y_non_zero, np.zeros_like(Z_non_zero), 1, 1, bar_height, color=color, shade=True)

        return ax

    ani = animation.FuncAnimation(
        fig, animate, frames=len(grid_array), interval=interval, blit=False
    )

    if gif is not None:
        print("Saving gif...")
        ani.save(gif + ".gif", writer="pillow", dpi=80)
        print("Gif saved.")

    plt.show()

def plot2D_seaborn(grid_array, interval=50, gif=None, colors=None):
    fig, ax = plt.subplots()
    ax.axis("off")

    # Set default colors if none provided
    if colors is None:
        colors = {1: "green", 2: "brown"}  # example colors for different types of terrain

    cmap = sns.color_palette([colors[val] for val in sorted(colors.keys())], as_cmap=True)

    def animate(i):
        ax.clear()
        ax.axis("off")
        Z = np.where(grid_array[i] == 0, np.nan, grid_array[i])
        sns.heatmap(Z, cmap=cmap, cbar=False, square=True, linewidths=0.1, linecolor='white', ax=ax)
        return ax

    ani = animation.FuncAnimation(
        fig, animate, frames=len(grid_array), interval=interval, blit=False
    )

    if gif is not None:
        print("Saving gif...")
        ani.save(gif + ".gif", writer="pillow", dpi=80)
        print("Gif saved.")

    plt.show()