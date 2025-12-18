"""
QUESTION:
Create a function `update_dataframe` that takes two pandas DataFrames `df1` and `df2` as input, with the same column names and row numbers but possibly different element values. The function should update the value of each element in `df1` to 1 if its corresponding value in `df2` is 1.
"""

import pandas as pd

def update_dataframe(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Updates the values of df1 to 1 if the corresponding value in df2 is 1.

    Args:
    df1 (pd.DataFrame): The DataFrame to be updated.
    df2 (pd.DataFrame): The DataFrame with values to check.

    Returns:
    pd.DataFrame: The updated DataFrame df1.
    """
    df1[df2 == 1] = 1
    return df1