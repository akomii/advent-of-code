import pandas as pd

data = pd.read_csv('input.txt', header=None, dtype=str)
data = data[0].apply(lambda x: pd.Series(list(x)))

GAMMA = ''
EPSILON = ''

for c in range(len(data.columns)):
    counts = data[c].value_counts()
    GAMMA += str(counts.idxmax())
    EPSILON += str(counts.idxmin())

GAMMA = int(GAMMA, 2)
EPSILON = int(EPSILON, 2)

print(GAMMA * EPSILON)
