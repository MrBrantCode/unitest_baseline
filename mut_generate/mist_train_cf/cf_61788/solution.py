"""
QUESTION:
Create a function called `filter_pivot_table` that takes a pivot table as input and filters rows with no value in two specific columns. The function should exclude any irrelevant information and only filter the pivot table, without affecting the rest of the data in the sheet. The function should return the filtered pivot table.
"""

import pandas as pd

def filter_pivot_table(pivot_table, column1, column2):
    """
    Filter rows with no value in two specific columns from a pivot table.

    Args:
    pivot_table (pd.DataFrame): The input pivot table.
    column1 (str): The name of the first column to filter.
    column2 (str): The name of the second column to filter.

    Returns:
    pd.DataFrame: The filtered pivot table.
    """

    # Filter rows with no value in both columns
    filtered_table = pivot_table[(~pivot_table[column1].isnull()) & (~pivot_table[column2].isnull())]
    
    return filtered_table