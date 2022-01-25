import random
from generate_chunk import generate_chunk
from display_terrain import display_terrain

seed_list = list(range(0, 1000))
seeds_using = [37]
just_content = False

# for x in range(10):
#     seeds_using.append(random.choice(seed_list))

for seed in seeds_using:
    my_chunk = generate_chunk(seed, 0, 0, 100, 8, 4)["noise"]
    my_figure = display_terrain(100, my_chunk, seed, show=False, justcontent=True if just_content else False)
    if just_content:
        my_figure.savefig("saved/" + str(seed), transparent=True, bbox_inches='tight', pad_inches=0)
    else:
        my_figure.savefig("saved/" + str(seed))
