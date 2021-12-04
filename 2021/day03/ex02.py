import pandas
import pandas as pd

data = pd.read_csv('input.txt', header=None, dtype=str)
data = data[0].apply(lambda x: pd.Series(list(x)))


def get_data_rating(df: pandas.DataFrame, mode: str) -> int:
    if mode == 'max':
        common_value = '1'
    elif mode == 'min':
        common_value = '0'
    for c in range(len(df.columns)):
        counts = df[c].value_counts()
        if (len(counts)) < 2:
            continue
        if counts[0] == counts[1]:
            most_common = common_value
        else:
            if mode == 'max':
                most_common = counts.idxmax()
            elif mode == 'min':
                most_common = counts.idxmin()
        df = df[df[c].isin([most_common])]
    rating_binary = [''.join(x) for x in df.values][0]
    return int(rating_binary, 2)


OXYGEN = get_data_rating(data.copy(), 'max')
CO2 = get_data_rating(data.copy(), 'min')

print(CO2 * OXYGEN)
