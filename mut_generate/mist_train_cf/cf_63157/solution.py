"""
QUESTION:
Create a function named `process_dataframes` that takes three parameters: two pandas dataframes `df1` and `df2`, and a string `sort_column` representing the column name to sort by. The function should concatenate `df1` and `df2` horizontally, replace missing values with the mean of the corresponding column, and sort the resulting dataframe by `sort_column`. If `sort_column` is not found in the resulting dataframe, the function should handle this error. Assume that `df1` and `df2` share a common key for merging.
"""

import pandas as pd
import numpy as np

def process_dataframes(df1, df2, sort_column):
    # Concatenate dataframes horizontally
    new_df = pd.concat([df1, df2], axis=1)

    # Replace missing(NaN) values with the mean of the corresponding column
    new_df = new_df.apply(lambda x: x.fillna(x.mean()),axis=0)

    # Error handling for non-existing column
    if sort_column not in new_df.columns:
        print(f"Error: The specified column '{sort_column}' not found.")
        return None

    # Sort dataframe by the specified column
    new_df = new_df.sort_values(sort_column)

    return new_df