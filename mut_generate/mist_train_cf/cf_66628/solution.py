"""
QUESTION:
Write a function named `remove_null_columns` that takes a Pandas DataFrame `df` as input and returns a new DataFrame with all columns containing any null or NaN values removed.
"""

import pandas as pd

def remove_null_columns(df):
    return df.dropna(axis=1)