"""
QUESTION:
Create a function named `filter_dataframe` that filters a pandas DataFrame based on multiple OR conditions applied to a specific column named "category" in a case-insensitive manner. The function should take the DataFrame and a list of strings as input, where the strings are the conditions to be applied to the "category" column. The function should return the filtered DataFrame.
"""

import pandas as pd

def filter_dataframe(df, conditions):
    """
    Filter a pandas DataFrame based on multiple OR conditions applied to the "category" column in a case-insensitive manner.

    Parameters:
    df (pd.DataFrame): The DataFrame to be filtered.
    conditions (list): A list of strings representing the conditions to be applied to the "category" column.

    Returns:
    pd.DataFrame: The filtered DataFrame.
    """
    # Apply the conditions using OR operator
    return df[pd.concat([df['category'].str.contains(condition, case=False) for condition in conditions], axis=1).any(axis=1)]