"""
QUESTION:
Write a function named `select_columns_and_rows` that takes a Pandas DataFrame `df` as input and returns a new DataFrame. The function should select rows where the 'Age' column is greater than 30 and the 'City' column is either 'Paris' or 'Tokyo'. Then, it should select the 'Name' and 'Salary' columns for the selected rows.
"""

import pandas as pd

def select_columns_and_rows(df):
    """
    Selects rows where the 'Age' column is greater than 30 and the 'City' column is either 'Paris' or 'Tokyo'. 
    Then, it selects the 'Name' and 'Salary' columns for the selected rows.

    Parameters:
    df (pandas DataFrame): Input DataFrame.

    Returns:
    pandas DataFrame: New DataFrame with the selected columns for the matching rows.
    """
    return df.loc[(df['Age'] > 30) & (df['City'].isin(['Paris', 'Tokyo'])), ['Name', 'Salary']]