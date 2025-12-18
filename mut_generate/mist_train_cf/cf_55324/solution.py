"""
QUESTION:
Write a function `get_min_time_rows` that takes a pandas DataFrame as input, containing columns "key" and "time". The function should return a new DataFrame with duplicate rows removed based on the "key" column, keeping only the row with the minimum "time" value for each "key" and dropping the rest. The function should preserve the original DataFrame index.
"""

def get_min_time_rows(df):
    return df.loc[df.groupby('key')['time'].idxmin()]