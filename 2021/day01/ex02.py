import csv
import numpy as np

with open('input.txt', 'r') as file:
    reader = csv.reader(file)
    list_input_items = np.array([int(row[0]) for row in reader])

list_average_items = np.convolve(list_input_items, np.ones(3), 'valid') / 3

NUM_INCREASES = sum([val > list_average_items[ind] for ind, val in enumerate(list_average_items[1:])])

print(NUM_INCREASES)
