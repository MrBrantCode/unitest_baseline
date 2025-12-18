"""
QUESTION:
Create a function `format_names` that takes a pandas DataFrame as input, modifies the 'Name' column by adding an underscore after the first four characters, removes leading zeros from the rest of the string, and returns the modified DataFrame. The function should maintain the original letters (first four characters) and only modify the numbers that follow.
"""

import pandas as pd

def format_names(df):
    """
    Modifies the 'Name' column by adding an underscore after the first four characters, 
    removes leading zeros from the rest of the string, and returns the modified DataFrame.

    Args:
    df (pd.DataFrame): Input DataFrame with a 'Name' column.

    Returns:
    pd.DataFrame: Modified DataFrame with the updated 'Name' column.
    """
    df['Name'] = df['Name'].apply(lambda x: x[:4] + '_' + str(int(x[4:])))
    return df