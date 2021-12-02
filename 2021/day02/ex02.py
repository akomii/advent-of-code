import pandas as pd

data = pd.read_csv('input.txt', sep=" ", header=None)

AIM = 0
DEPTH = 0
POS_HORZ = 0

for index, row in data.iterrows():
    if row[0] == 'forward':
        POS_HORZ += row[1]
        DEPTH += AIM * row[1]
    elif row[0] == 'up':
        AIM -= row[1]
    elif row[0] == 'down':
        AIM += row[1]

print(DEPTH * POS_HORZ)
