"""
QUESTION:
Write a function named `filter_dataframe` that takes a pandas DataFrame as input and returns the DataFrame with rows excluded where the 'Age' is less than 18 and the 'Name' starts with the letter 'A'.
"""

import pandas as pd

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function filters a pandas DataFrame to exclude rows where 'Age' is less than 18 and 'Name' starts with the letter 'A'.

    Args:
        df (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: Filtered DataFrame
    """
    return df.loc[(df['Age'] >= 18) & (~df['Name'].str.startswith('A'))]