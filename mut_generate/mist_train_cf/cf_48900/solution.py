"""
QUESTION:
Write a function `modify_column_names` that takes a pandas DataFrame as input. The function should modify the DataFrame by prefixing all column names that consist only of digits with a specified string. The modified DataFrame should be returned. The function should not take any other arguments besides the DataFrame. The prefixed string should be 'col_'.
"""

import pandas as pd

def modify_column_names(df):
    """
    This function takes a pandas DataFrame as input, prefixes all column names 
    that consist only of digits with 'col_', and returns the modified DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The modified DataFrame.
    """
    return df.rename(columns=lambda x: 'col_' + str(x) if x.isdigit() else x)