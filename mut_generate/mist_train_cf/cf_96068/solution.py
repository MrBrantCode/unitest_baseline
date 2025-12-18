"""
QUESTION:
Filter a Pandas DataFrame column using multiple OR conditions in a case-insensitive manner while optimizing for time complexity. The function should take a DataFrame, a column name, and a list of conditions as inputs.
"""

import pandas as pd

def filter_dataframe(df, column, conditions):
    """
    Filter a Pandas DataFrame column using multiple OR conditions in a case-insensitive manner.

    Args:
        df (pd.DataFrame): The input DataFrame.
        column (str): The name of the column to filter.
        conditions (list): A list of conditions to filter by.

    Returns:
        pd.DataFrame: The filtered DataFrame.
    """
    return df[df[column].str.contains('|'.join(conditions), case=False, regex=True)]