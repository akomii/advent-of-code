import pandas as pd
import numpy as np


def convert_txt_to_df(file: str) -> pd.DataFrame:
    df = pd.read_csv(file, header=None, dtype=str, delimiter=' ')
    df[['x1', 'y1']] = df[0].str.split(',', expand=True)
    df[['x2', 'y2']] = df[2].str.split(',', expand=True)
    df.drop(columns=[0, 1, 2], inplace=True)
    return df.astype(int)


def draw_coordinate_lines_into_2d_array(df: pd.DataFrame) -> np.ndarray:
    arr = np.zeros((1000, 1000))
    for index, row in df.iterrows():
        if row['x1'] == row['x2'] or row['y1'] == row['y2']:
            if row['x1'] > row['x2']:
                arr[row['y1']:row['y2'] + 1, row['x2']:row['x1'] + 1] += 1
            elif row['y1'] > row['y2']:
                arr[row['y2']:row['y1'] + 1, row['x1']:row['x2'] + 1] += 1
            else:
                arr[row['y1']:row['y2'] + 1, row['x1']:row['x2'] + 1] += 1
        else:
            if row['x1'] > row['x2'] and row['y1'] > row['y2']:
                for x in range(row['x1'] - row['x2'] + 1):
                    arr[row['y2'] + x, row['x2'] + x] += 1
            elif row['x1'] < row['x2'] and row['y1'] > row['y2']:
                for x in range(row['x2'] - row['x1'] + 1):
                    arr[row['y1'] - x, row['x1'] + x] += 1
            elif row['x1'] > row['x2'] and row['y1'] < row['y2']:
                for x in range(row['x1'] - row['x2'] + 1):
                    arr[row['y2'] - x, row['x2'] + x] += 1
            else:
                for x in range(row['x2'] - row['x1'] + 1):
                    arr[row['y1'] + x, row['x1'] + x] += 1
    return arr


def count_overlapping_lines_in_2d_array(arr: np.ndarray) -> int:
    return np.count_nonzero(arr > 1)


if __name__ == "__main__":
    data = convert_txt_to_df('input.txt')
    diag = draw_coordinate_lines_into_2d_array(data)
    print(count_overlapping_lines_in_2d_array(diag))
