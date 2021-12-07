data: list = list(map(int, open('input.txt').read().split(',')))
data.sort()

val_median = data[round(len(data)/2)]

for idx, _ in enumerate(data.copy()):
    data[idx] = abs(data[idx] - val_median)

print(sum(data))
