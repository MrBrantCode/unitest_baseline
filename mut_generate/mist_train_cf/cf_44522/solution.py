"""
QUESTION:
Create two Python functions using the Pandas library: `identify_missing` and `remove_missing`. 

The `identify_missing` function takes a Pandas dataframe and a list of column names as input, and returns the indices of rows where any of the specified columns contain missing values.

The `remove_missing` function takes a Pandas dataframe and a list of indices as input, and returns a new dataframe with the rows at the specified indices removed. 

The function should correctly identify and remove rows with missing values in the specified columns, without losing data from other columns.
"""

import pandas as pd

def entrance(df, cols):
    # From the dataframe, select rows where the column value is null
    missing_indices = df.index[df[cols].isnull().any(axis=1)]
    df_clean = df.drop(missing_indices)
    return df_clean