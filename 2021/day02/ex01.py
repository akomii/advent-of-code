import pandas as pd

data = pd.read_csv('input.txt', sep=" ", header=None)

list_forward = data[data[0] == 'forward']
NUM_FORWARD = sum(list_forward[1].tolist())

list_up = data[data[0] == 'up']
NUM_UP = sum(list_up[1].tolist())

list_down = data[data[0] == 'down']
NUM_DOWN = sum(list_down[1].tolist())

print(NUM_FORWARD * (NUM_DOWN - NUM_UP))
