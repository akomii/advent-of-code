import pandas as pd
import numpy as np


def convert_txt_to_df(file: str) -> pd.DataFrame:
    df = pd.read_csv(file, header=None, dtype=str, delimiter=' ')
    df[['x1', 'y1']] = df[0].str.split(',', expand=True)
    df[['x2', 'y2']] = df[2].str.split(',', expand=True)
    df.drop(columns=[0, 1, 2], inplace=True)
    return df.astype(int)


def filter_df_for_vert_and_horz_lines(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df['x1'] == df['x2']) | (df['y1'] == df['y2'])]


def fix_order_of_df_coordinates(df: pd.DataFrame) -> pd.DataFrame:
    df[['x1', 'x2']] = df[['x1', 'x2']].mask(df['x1'] > df['x2'], df[['x2', 'x1']].values)
    df[['y1', 'y2']] = df[['y1', 'y2']].mask(df['y1'] > df['y2'], df[['y2', 'y1']].values)
    return df


def draw_coordinate_lines_into_2d_array(df: pd.DataFrame) -> np.ndarray:
    arr = np.zeros((1000, 1000))
    for index, row in df.iterrows():
        arr[row['y1']:row['y2'] + 1, row['x1']:row['x2'] + 1] += 1
    return arr


def count_overlapping_lines_in_2d_array(arr: np.ndarray) -> int:
    return np.count_nonzero(arr > 1)


if __name__ == "__main__":
    data = convert_txt_to_df('input.txt')
    data = filter_df_for_vert_and_horz_lines(data)
    data = fix_order_of_df_coordinates(data)
    diag = draw_coordinate_lines_into_2d_array(data)
    print(count_overlapping_lines_in_2d_array(diag))
