import numpy as np
import matplotlib.pyplot as plt
import math

from generate_chunk import generate_chunk
from display_terrain import display_terrain


seed = int(input("Input seed: "))
chunk_x = int(input("Input chunk_x: "))
chunk_y = int(input("Input chunk_y: "))
size = 16


noise_array = generate_chunk(seed, chunk_x, chunk_y, size)


# x = np.arange(size)
# y = x.copy()
# x, y = np.meshgrid(x, y)
# z = np.array(noise_array).reshape(size, size)
#
# fig = plt.figure()
# ax = plt.axes(projection ='3d')
# ax.set_zlim(bottom=0, top=80)
#
# ax.plot_surface(x, y, z, cmap ='viridis', edgecolor ='green')
# ax.set_title("Terrain Generation Test: Seed: " + str(seed) + ", chunk: (" + str(chunk_x) + ", " + str(chunk_y) + ")")
# plt.show()

display_terrain(size, noise_array, seed, chunk_x, chunk_y)
