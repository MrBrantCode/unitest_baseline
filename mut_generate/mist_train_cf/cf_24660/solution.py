"""
QUESTION:
Create a function `calculate_row_averages` that takes a pandas DataFrame as input and returns the same DataFrame with an additional column 'avg' containing the average of each row's elements. The input DataFrame can have any number of rows and columns, and the elements are numeric.
"""

import pandas as pd

def calculate_row_averages(df):
    """
    This function takes a pandas DataFrame as input and returns the same DataFrame 
    with an additional column 'avg' containing the average of each row's elements.

    Parameters:
    df (pd.DataFrame): A pandas DataFrame with numeric elements.

    Returns:
    pd.DataFrame: The input DataFrame with an additional 'avg' column.
    """
    df['avg'] = df.mean(axis=1)
    return df