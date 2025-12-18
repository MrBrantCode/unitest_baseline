"""
QUESTION:
Write a function called `convert_df_to_list` that takes a pandas DataFrame as input and returns a standard Python list. The function should replace all missing or NaN values in the DataFrame with a default value of 0. The solution should prioritize computational efficiency.
"""

import pandas as pd
import numpy as np

def convert_df_to_list(df):
    """
    Convert a pandas DataFrame to a standard Python list, replacing missing or NaN values with 0.

    Args:
        df (pd.DataFrame): Input DataFrame

    Returns:
        list: Python list representation of the DataFrame
    """
    df.fillna(0, inplace=True)
    return df.values.tolist()