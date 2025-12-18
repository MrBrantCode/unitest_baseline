"""
QUESTION:
Write a function `f(df)` that takes a pandas DataFrame `df` as input and returns the modified DataFrame where values in each column that appear less than 2 times are replaced with 'others'.
"""

import pandas as pd

def f(df):
    """
    Replaces values in each column of a DataFrame that appear less than 2 times with 'others'.

    Args:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: The modified DataFrame with rare values replaced.
    """
    for col in df.columns:
        mask = df[col].map(df[col].value_counts()) < 2
        df.loc[mask, col] = 'others'
    return df