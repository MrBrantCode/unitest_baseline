"""
QUESTION:
Write a function `replace_nan_with_string` that takes a Pandas dataframe as input and replaces all NaN values with a given string. The function should return the modified dataframe. The input dataframe can have any shape and any type of data, but it should be able to handle non-string data.
"""

import pandas as pd
import numpy as np

def replace_nan_with_string(df, string):
    """
    Replaces all NaN values in a Pandas dataframe with a given string.

    Args:
        df (pd.DataFrame): The input dataframe.
        string (str): The string to replace NaN values with.

    Returns:
        pd.DataFrame: The modified dataframe with NaN values replaced.
    """
    return df.where(pd.notnull(df), string)