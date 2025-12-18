"""
QUESTION:
Design a function named `count_missing_values` that calculates and returns the total number of missing values in a given DataFrame. The function should take a pandas DataFrame as input and return an integer.
"""

import pandas as pd

def count_missing_values(df):
    """
    This function calculates the total number of missing values in a specific dataframe.

    Parameters:
    df (DataFrame): Dataframe to check for missing values

    Returns:
    int: total missing values in the dataframe
    """
    return df.isnull().sum().sum()