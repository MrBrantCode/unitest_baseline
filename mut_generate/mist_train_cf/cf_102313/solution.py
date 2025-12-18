"""
QUESTION:
Write a function `filter_and_sort_df` that takes a pandas DataFrame as input, filters out rows where the 'Age' is less than 18 and the 'Name' starts with the letter 'A', and returns the resulting DataFrame sorted in descending order by 'Age'.
"""

import pandas as pd

def filter_and_sort_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filters out rows where the 'Age' is less than 18 and the 'Name' starts with the letter 'A', 
    and returns the resulting DataFrame sorted in descending order by 'Age'.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The filtered and sorted DataFrame.
    """
    return df[(df['Age'] >= 18) & (~df['Name'].str.startswith('A'))].sort_values(by='Age', ascending=False)