import math
import sys
from generate_chunk import generate_chunk
from display_terrain import display_terrain

if "-h" in sys.argv or "--help" in sys.argv:
    print("-- FLYNN TERRAIN GENERATION HELP --")
    print()
    print("Options:")
    print("-s [seed]           : Set generation seed              (default: 12345)")
    print("-w [world_size]     : Set world width/height in chunks (default: 3)")
    print("-z [size]           : Set chunk size                   (default: 16)")
    print("-f [hill_frequency] : Change frequency of hills        (default: 3)")
    print("-g [hill_height]    : Change height of hills           (default: 5)")
    quit()

# seed = int(input("Input seed: "))
# world_size = int(input("Input world_size: "))
seed = 12345
world_size = 3
size = 16
hill_frequency = 3
hill_height = 5
if "-s" in sys.argv:
    seed = int(sys.argv[sys.argv.index("-s") + 1])
if "-w" in sys.argv:
    world_size = int(sys.argv[sys.argv.index("-w") + 1])
if "-z" in sys.argv:
    size = int(sys.argv[sys.argv.index("-z") + 1])
if "-f" in sys.argv:
    hill_frequency = int(sys.argv[sys.argv.index("-f") + 1])
if "-g" in sys.argv:
    hill_height = int(sys.argv[sys.argv.index("-g") + 1])

temp_noise_array = []

start_chunk = 0 - math.trunc(world_size / 2)
for chunk_y in range(world_size):
    chunk_y += start_chunk
    for chunk_x in range(world_size):
        chunk_x += start_chunk
        temp_noise_array.append(generate_chunk(seed, chunk_x, chunk_y, size, hill_frequency, hill_height)["noise"])

noise_array = []
for chunk_row in range(world_size):
    for chunk_index in range(size):
        for transfer_chunk in range(world_size):
            noise_array += temp_noise_array[transfer_chunk + chunk_row*world_size][chunk_index*size:chunk_index*size+size]

display_terrain(size, noise_array, seed, world_size=world_size, start_coord=start_chunk*size)
