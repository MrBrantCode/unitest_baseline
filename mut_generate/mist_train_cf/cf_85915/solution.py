"""
QUESTION:
Write a function `replace_non_numeric_with_mean` that takes a Pandas DataFrame as input, filters out non-numeric values, computes the mean for each column, and updates each non-numeric value with the corresponding column's mean. The function should return the updated DataFrame.
"""

import pandas as pd

def replace_non_numeric_with_mean(df):
    """
    Replaces non-numeric values in a DataFrame with the mean of their respective columns.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: The DataFrame with non-numeric values replaced with the mean of their columns.
    """
    # Convert non-numerical columns to numeric types
    df = df.apply(pd.to_numeric, errors='coerce')

    # Compute the mean of each column, ignoring NaN values
    means = df.mean(skipna=True)

    # Fill NaN values with the column means
    df = df.fillna(means)

    return df