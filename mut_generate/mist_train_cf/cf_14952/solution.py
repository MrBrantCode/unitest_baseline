"""
QUESTION:
Write a function `get_unique_positive_quantities` that takes no arguments. It should return all unique positive numbers from the 'quantity' column in the 'Orders' table.
"""

import pandas as pd

def get_unique_positive_quantities(df):
    """
    Returns all unique positive numbers from the 'quantity' column in the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame representing the 'Orders' table.

    Returns:
        list: A list of unique positive quantities.
    """
    return df.loc[df['quantity'] > 0, 'quantity'].unique().tolist()