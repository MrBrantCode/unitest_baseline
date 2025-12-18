"""
QUESTION:
Replace NaN and None with 0 in a given DataFrame column.

Write a function `replace_nan_with_zero` that takes a pandas DataFrame `df` and a column name `column_name` as input, and returns the DataFrame with all NaN and None values in the specified column replaced with 0. The function should not modify the original DataFrame.
"""

import pandas as pd
import numpy as np

def replace_nan_with_zero(df, column_name):
    """
    Replaces NaN and None values in the specified column of a pandas DataFrame with 0.

    Args:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The name of the column to replace NaN and None values in.

    Returns:
        pd.DataFrame: A new DataFrame with NaN and None values replaced with 0.
    """
    # Create a copy of the original DataFrame to avoid modifying it
    df_copy = df.copy()
    
    # Use the fillna method to replace NaN and None values with 0 in the specified column
    df_copy[column_name] = df_copy[column_name].fillna(0)
    
    return df_copy