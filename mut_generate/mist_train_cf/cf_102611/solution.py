"""
QUESTION:
Write a function named `purge_and_sort_df` that takes a Pandas DataFrame as input, removes all rows with a negative value in the 'Age' column, and returns the resulting DataFrame sorted in descending order by the 'Age' column. The function should not modify the original DataFrame and should return a new sorted DataFrame.
"""

import pandas as pd

def purge_and_sort_df(df):
    """
    This function takes a Pandas DataFrame as input, removes all rows with a negative value 
    in the 'Age' column, and returns the resulting DataFrame sorted in descending order by 
    the 'Age' column.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: A new DataFrame with rows filtered by Age and sorted in descending order.
    """
    # Create a copy of the DataFrame to avoid modifying the original
    df_copy = df.copy()
    
    # Filter the rows by keeping only the rows where the Age column has a value greater than or equal to 0
    df_copy = df_copy[df_copy['Age'] >= 0]
    
    # Sort the remaining rows based on the Age column in descending order
    df_copy = df_copy.sort_values(by='Age', ascending=False)
    
    # Return the resulting DataFrame
    return df_copy