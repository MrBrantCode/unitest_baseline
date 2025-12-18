"""
QUESTION:
Find the second largest value in the column 'A' of a given dataframe in O(nlogn) time complexity using Python, where the function should accept the dataframe as input and return the second largest value.
"""

import pandas as pd

def find_second_largest(df):
    """
    Find the second largest value in the column 'A' of a given dataframe.

    Args:
        df (pd.DataFrame): Input dataframe.

    Returns:
        The second largest value in column 'A'.
    """
    values = df['A'].values.tolist()
    sorted_values = sorted(values, reverse=True)
    return sorted_values[1]