"""
QUESTION:
Write a function named `replace_nan` that takes a pandas DataFrame and a replacement value as input and returns the DataFrame with all NaN values replaced by the given value. The function should be able to handle different data types in the DataFrame, including cases where there are multiple NaN values per row or column, while optimizing performance for large datasets.
"""

import pandas as pd
import numpy as np

def replace_nan(df, value):
    """
    The function receives a dataframe and a value. It returns the dataframe with NaN values replaced by the value received.
    """
    
    return df.fillna(value)