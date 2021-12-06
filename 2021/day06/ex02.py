import numpy as np

data: list = np.loadtxt('input.txt', delimiter=',').tolist()

dict_fishes = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

values, counts = np.unique(data, return_counts=True)

for idx, _ in enumerate(counts):
    dict_fishes[values[idx]] = counts[idx]

for day in range(256):
    fishes_new = dict_fishes[0]
    for x in range(8):
        dict_fishes[x] = dict_fishes[x + 1]
    dict_fishes[6] += fishes_new
    dict_fishes[8] = fishes_new

print(sum(dict_fishes.values()))

