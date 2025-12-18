"""
QUESTION:
Create a function called `merge_dataframes` that takes two pandas dataframes (`df1` and `df2`) and a column name (`column_name`) as input. The function should merge the two dataframes based on the specified column and return the resulting dataframe. The merge operation should be an inner join, meaning only the rows with matching values in the specified column should be included in the result.
"""

import pandas as pd

def merge_dataframes(df1, df2, column_name):
    """
    Merge two pandas dataframes based on a specific column.

    Args:
    - df1 (pd.DataFrame): The first dataframe.
    - df2 (pd.DataFrame): The second dataframe.
    - column_name (str): The column name to merge on.

    Returns:
    - pd.DataFrame: The merged dataframe.
    """
    return pd.merge(df1, df2, on=column_name)