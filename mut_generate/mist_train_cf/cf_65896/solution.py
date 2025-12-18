"""
QUESTION:
Create a function called `repeat_rows_by_duration` that takes a pandas DataFrame with columns 'event', 'budget', and 'duration_days' as input, where 'budget' and 'duration_days' are initially strings. The function should repeat each row based on the value in 'duration_days', convert 'budget' and 'duration_days' to integers, and return the resulting DataFrame.
"""

import pandas as pd

def repeat_rows_by_duration(df):
    """
    Repeat each row in a DataFrame based on the 'duration_days' column and convert 'budget' and 'duration_days' to integers.

    Args:
    df (pd.DataFrame): A DataFrame with columns 'event', 'budget', and 'duration_days'.

    Returns:
    pd.DataFrame: The resulting DataFrame with repeated rows and 'budget' and 'duration_days' converted to integers.
    """
    df[['budget', 'duration_days']] = df[['budget', 'duration_days']].astype(int)
    return df.loc[df.index.repeat(df['duration_days'])].reset_index(drop=True)