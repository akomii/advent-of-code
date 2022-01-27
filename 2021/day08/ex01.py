import pandas as pd

df = pd.read_csv('input.txt', header=None, dtype=str, delimiter=' ')

df_input = df.iloc[:, :10]
df_output = df.iloc[:, 11:]

NUM_ONE: int = 0
NUM_FOUR: int = 0
NUM_SEVEN: int = 0
NUM_EIGHT: int = 0

for column in df_output:
    NUM_ONE += sum(df_output[column].str.len() == 2)
    NUM_FOUR += sum(df_output[column].str.len() == 4)
    NUM_SEVEN += sum(df_output[column].str.len() == 3)
    NUM_EIGHT += sum(df_output[column].str.len() == 7)

print(NUM_ONE + NUM_FOUR + NUM_SEVEN + NUM_EIGHT)
