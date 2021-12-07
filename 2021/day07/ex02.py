data: list = list(map(int, open('input.txt').read().split(',')))

fuel_cost_summed = []

for x in range(min(data), max(data) + 1):
    tmp_data = data.copy()
    for idx, _ in enumerate(tmp_data.copy()):
        steps = abs(tmp_data[idx] - x)
        tmp_data[idx] = int((steps * (steps + 1)) / 2)
    fuel_cost_summed.append(sum(tmp_data))

print(min(fuel_cost_summed))
