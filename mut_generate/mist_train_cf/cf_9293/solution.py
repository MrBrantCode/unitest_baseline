"""
QUESTION:
Create a function called `create_dataframe` that takes a dictionary of lists as input where the keys represent column names and the values represent column values. The function should return a Pandas DataFrame with column names in uppercase, column values in lowercase, and sorted in descending order based on the 'Sales' column.
"""

import pandas as pd

def create_dataframe(data):
    """
    Create a Pandas DataFrame from a dictionary of lists, 
    with column names in uppercase and column values in lowercase, 
    and sorted in descending order based on the 'Sales' column.

    Args:
        data (dict): A dictionary of lists where keys represent column names and values represent column values.

    Returns:
        pd.DataFrame: A Pandas DataFrame with column names in uppercase, column values in lowercase, 
        and sorted in descending order based on the 'Sales' column.
    """
    df = pd.DataFrame(data)
    df.columns = df.columns.str.upper()
    for col in df.columns:
        if col != 'SALES':
            df[col] = df[col].astype(str).str.lower()
    df = df.sort_values('SALES', ascending=False)
    return df