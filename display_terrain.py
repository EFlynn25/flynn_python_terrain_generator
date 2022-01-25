import numpy as np
import matplotlib.pyplot as plt
import math

def display_terrain(size, noise_array, seed=None, chunk_x=None, chunk_y=None, world_size=1, start_coord=0, show=True, justcontent=False):
    x = np.array(list(range(start_coord, start_coord+world_size*size)))
    y = x.copy()
    x, y = np.meshgrid(x, y)
    z = np.array(noise_array).reshape(world_size*size, world_size*size)

    fig = plt.figure()
    ax = plt.axes(projection ='3d')
    if justcontent:
        ax.set_zlim(bottom=20, top=100)
        ax.set_axis_off()
    else:
        ax.set_zlim(bottom=0, top=80)

    ax.plot_surface(x, y, z, cmap ='viridis', edgecolor ='green')
    if not justcontent:
        title_string = "Flynn Terrain Generation Test"
        if seed != None:
            title_string += " - Seed: " + str(seed)
            if chunk_x != None and chunk_y != None:
                title_string += ", chunk: (" + str(chunk_x) + ", " + str(chunk_y) + ")"
            elif world_size > 1:
                title_string += ", world size: " + str(world_size)
        ax.set_title(title_string)
    if show:
        plt.show()
    return fig
