"""
QUESTION:
Write a function named `filter_and_sort_dataframe` that takes a pandas DataFrame as input. The DataFrame contains two columns: 'Name' and 'Age'. The function should return a new DataFrame that excludes any rows where the 'Age' is less than 18 and the 'Name' starts with the letter 'A'. The returned DataFrame should be sorted in descending order based on the 'Age' column.
"""

import pandas as pd

def filter_and_sort_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function filters a DataFrame to exclude rows where 'Age' is less than 18 
    and 'Name' starts with 'A', then sorts the result in descending order by 'Age'.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: The filtered and sorted DataFrame.
    """
    return df[(df['Age'] >= 18) & (~df['Name'].str.startswith('A'))].sort_values(by='Age', ascending=False)