"""
QUESTION:
Write a function named `stack_dataframe` that reshapes a given DataFrame by stacking its columns, similar to the pandas `stack()` function, while minimizing memory allocation. The function should take a pandas DataFrame as input and return a reshaped DataFrame with minimal additional memory usage.
"""

import pandas as pd
import numpy as np

def stack_dataframe(df):
    """
    Reshapes a given DataFrame by stacking its columns, similar to the pandas stack() function, 
    while minimizing memory allocation.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Reshaped DataFrame with minimal additional memory usage.
    """

    # Convert DataFrame to a numpy array to reduce memory usage
    arr = df.to_numpy()

    # Get the number of rows and columns in the DataFrame
    num_rows, num_cols = arr.shape

    # Reshape the numpy array
    reshaped_arr = arr.reshape(-1, 1)

    # Create a new DataFrame with the reshaped array
    reshaped_df = pd.DataFrame(reshaped_arr, columns=['stacked_column'])

    return reshaped_df