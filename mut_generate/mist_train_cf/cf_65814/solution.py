"""
QUESTION:
Write a function `convert_column_to_int` that takes a pandas DataFrame and a column name as input, removes commas from the specified column, and converts it to integer type. Assume the column contains numeric values with commas as thousand separators and does not contain any null values.
"""

import pandas as pd

def convert_column_to_int(df, column_name):
    """
    Removes commas from the specified column in a pandas DataFrame and converts it to integer type.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to convert.
    
    Returns:
    pd.DataFrame: The DataFrame with the specified column converted to integer type.
    """
    df[column_name] = df[column_name].str.replace(',', '').astype(int)
    return df