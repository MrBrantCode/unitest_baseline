"""
QUESTION:
Given a pandas DataFrame `df` with a column `sea_level_0m`, write a function `calculate_rolling_mean_and_difference` that calculates the rolling mean of `sea_level_0m` with a window size of 240 and the difference between `sea_level_0m` and its rolling mean, and returns the modified DataFrame with the new columns `pandas_l` and `pandas_h`. The solution should be memory-efficient and not use the iris library.
"""

import pandas as pd

def entrance(df):
    window_size = 240
    rolling_mean = df['sea_level_0m'].rolling(window=window_size, center=True, min_periods=1).mean()
    df['pandas_l'] = rolling_mean
    df['pandas_h'] = df['sea_level_0m'] - rolling_mean
    return df