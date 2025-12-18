"""
QUESTION:
Write a function `drop_all_missing_rows` that takes a Pandas dataframe as input and returns a new dataframe with all rows that contain only missing values dropped.
"""

import pandas as pd

def drop_all_missing_rows(df):
    """
    This function takes a Pandas dataframe as input and returns a new dataframe with all rows that contain only missing values dropped.

    Parameters:
    df (Pandas DataFrame): The input dataframe.

    Returns:
    Pandas DataFrame: A new dataframe with all rows that contain only missing values dropped.
    """
    return df.dropna(how='all')