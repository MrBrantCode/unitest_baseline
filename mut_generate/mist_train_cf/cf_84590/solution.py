"""
QUESTION:
Write a function `drop_columns_by_null_percentage` that takes a Pandas DataFrame `df` and an integer `p` (0-100) as input. The function should first drop all columns with any missing values from `df` and then filter out columns that have less than `p` percentage of non-null values.
"""

import pandas as pd

def drop_columns_by_null_percentage(df, p):
    """
    Drops columns with any missing values from the DataFrame and then filters out columns 
    that have less than a specified percentage of non-null values.

    Parameters:
    df (DataFrame): Input DataFrame
    p (int): Percentage of non-null values required (0-100)

    Returns:
    DataFrame: Filtered DataFrame
    """
    # Drop columns with any missing value
    df = df.dropna(axis=1, how='any')
    
    # Filter out columns that have less than a specified percentage of non-null values
    df = df[df.columns[df.count()/len(df) >= p/100]]
    
    return df