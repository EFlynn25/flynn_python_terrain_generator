from opensimplex import OpenSimplex

def generate_chunk(seed, chunk_x, chunk_y, size, hill_frequency=3, hill_height=5):
    tmp = OpenSimplex(seed)

    x_array = list(range(size*chunk_x, size*(chunk_x+1)))
    y_array = list(range(size*chunk_y, size*(chunk_y+1)))
    noise_array = []

    for y in range(size):
        y += chunk_y * size
        for x in range(size):
            x += chunk_x * size
            my_val = (tmp.noise2(x=hill_frequency*x/200, y=hill_frequency*y/200) + 1) * (hill_height * 3) + (60 - (hill_height * 3))
            noise_array.append(my_val)

    return {"x": x_array, "y": y_array, "noise": noise_array}
