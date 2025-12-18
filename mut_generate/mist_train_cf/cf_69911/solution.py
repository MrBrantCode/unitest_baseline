"""
QUESTION:
Convert a pandas DataFrame to a Standard Python List.

Write a function `convert_df_to_list` that takes a pandas DataFrame as input and returns a standard Python list. The function should handle DataFrames with various data types (string, int, float) and NaN values.

Note: The function should not use any external libraries other than pandas, and should not print any output. It should only return the converted list.
"""

import pandas as pd

def convert_df_to_list(df):
    """
    This function takes a pandas DataFrame as input and returns a standard Python list.
    
    Parameters:
    df (pd.DataFrame): The input pandas DataFrame.
    
    Returns:
    list: A standard Python list converted from the input DataFrame.
    """
    return df.values.tolist()