"""
QUESTION:
Write a function `filter_df_by_category` that filters a given Pandas DataFrame by a specific column named "category" using multiple OR conditions, ensuring the filtering is case-insensitive. The function should return the filtered DataFrame. 

The function should take two parameters: `df` (the input DataFrame) and `conditions` (a list of strings to be matched in the "category" column). The function should optimize for time complexity using vectorized operations provided by Pandas.
"""

import pandas as pd

def filter_df_by_category(df, conditions):
    """
    Filters a given Pandas DataFrame by a specific column named "category" using multiple OR conditions, ensuring the filtering is case-insensitive.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    conditions (list): A list of strings to be matched in the "category" column.
    
    Returns:
    pd.DataFrame: The filtered DataFrame.
    """
    conditions = [df['category'].str.contains(cond, case=False) for cond in conditions]
    return df[pd.concat(conditions, axis=1).any(axis=1)]