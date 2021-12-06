import numpy as np

data: list = np.loadtxt('input.txt', delimiter=',').tolist()

for day in range(80):
    list_new_fish = []
    for idx, _ in enumerate(data.copy()):
        if data[idx] == 0:
            list_new_fish.append(8)
            data[idx] = 6
        else:
            data[idx] -= 1
    data.extend(list_new_fish)

print(len(data))

