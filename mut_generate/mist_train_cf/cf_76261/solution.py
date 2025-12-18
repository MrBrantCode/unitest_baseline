"""
QUESTION:
Write a function to remove all spaces from the strings in a specified column of a pandas DataFrame.

The function should take a pandas DataFrame and a column name as input. It should return the DataFrame with all spaces removed from the strings in the specified column. The function should not create any additional columns, and it should directly modify the original DataFrame. The function should not throw any errors if the column contains non-string values.
"""

import pandas as pd

def remove_spaces_from_column(df, column_name):
    """
    Removes all spaces from the strings in a specified column of a pandas DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The name of the column to remove spaces from.

    Returns:
        pd.DataFrame: The DataFrame with spaces removed from the specified column.
    """
    df[column_name] = df[column_name].str.replace(" ", "")
    return df