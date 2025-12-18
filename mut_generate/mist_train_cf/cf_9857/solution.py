"""
QUESTION:
Implement a function `interpolate_missing_values` that takes a Pandas DataFrame `df` as input and returns the DataFrame with missing values interpolated based on the values of neighboring data points. The function should have a time complexity of O(n) and be able to handle datasets with up to 1 million rows.
"""

import pandas as pd

def interpolate_missing_values(df):
    # Sort the DataFrame by time if it's not already sorted
    if not df.index.is_monotonic_increasing:
        df = df.sort_index()

    # Interpolate missing values using linear interpolation
    df = df.interpolate(method='linear')

    return df