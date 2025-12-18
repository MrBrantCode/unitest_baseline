"""
QUESTION:
Create a function `access_or_create_column` that takes a pandas DataFrame and a column name as input. The function should return the specified column if it exists in the DataFrame. If the column does not exist, it should create the column with a default value of 0 and return the newly created column.
"""

import pandas as pd

def access_or_create_column(df, column_name):
    """
    Access or create a column in a pandas DataFrame.

    Args:
    - df (pd.DataFrame): Input DataFrame.
    - column_name (str): Name of the column to access or create.

    Returns:
    - pd.Series: The specified column if it exists, otherwise a new column with default value 0.
    """
    if column_name in df.columns:
        return df[column_name]
    else:
        df[column_name] = 0
        return df[column_name]