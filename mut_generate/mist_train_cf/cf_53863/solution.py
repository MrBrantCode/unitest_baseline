"""
QUESTION:
Filter a DataFrame where a column contains lists of values based on multiple conditions.

Create a function `filter_list_column` that takes a pandas DataFrame `df` and a list of items `items_to_look_for` as input, and returns a filtered DataFrame where the column 'values' contains any of the items in `items_to_look_for`. The function should work for any type of elements in the lists (numbers, strings, etc.). The DataFrame is expected to have a column named 'values' that contains lists as its values.
"""

import pandas as pd

def filter_list_column(df, items_to_look_for):
    """
    Filter a DataFrame where a column contains lists of values based on multiple conditions.
    
    Parameters:
    df (pd.DataFrame): DataFrame to be filtered
    items_to_look_for (list): List of items to look for in the 'values' column
    
    Returns:
    pd.DataFrame: Filtered DataFrame
    """
    return df[df['values'].apply(lambda row: any((i in row for i in items_to_look_for)))]