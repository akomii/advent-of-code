import csv

with open('input.txt', 'r') as file:
    reader = csv.reader(file)
    list_input_items = [int(row[0]) for row in reader]

NUM_INCREASES = sum([val > list_input_items[ind] for ind, val in enumerate(list_input_items[1:])])

print(NUM_INCREASES)
