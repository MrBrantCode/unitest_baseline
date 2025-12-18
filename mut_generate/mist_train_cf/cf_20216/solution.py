"""
QUESTION:
Write a function called `sum_dataframe_elements` that calculates the sum of all elements in a given pandas DataFrame. The function should take a pandas DataFrame as input and return the sum of its elements. Assume the DataFrame contains only numerical values and can be of any size.
"""

import pandas as pd

def sum_dataframe_elements(df):
    """
    Calculate the sum of all elements in a given pandas DataFrame.

    Args:
        df (pd.DataFrame): A pandas DataFrame containing numerical values.

    Returns:
        float: The sum of all elements in the DataFrame.

    """
    return df.values.sum()