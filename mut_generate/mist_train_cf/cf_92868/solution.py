"""
QUESTION:
Create a function named `select_rows` that takes a Pandas DataFrame `df`, a column name `column`, and a value as input. The function should return all rows from the DataFrame where the value in the specified column is equal to the given value. If the specified column does not exist in the DataFrame, the function should return an error message.
"""

import pandas as pd

def select_rows(df, column, value):
    """
    Selects all rows from a Pandas DataFrame where a column value is equal to a given value.

    Args:
        df (pd.DataFrame): The input DataFrame.
        column (str): The column name to filter by.
        value: The value to filter by.

    Returns:
        pd.DataFrame: A DataFrame with the selected rows. If the column does not exist, returns an error message.
    """
    if column not in df.columns:
        return f"Error: {column} column does not exist in the DataFrame."
    
    selected_rows = df[df[column] == value]
    return selected_rows