"""
ORIGINAL QUESTION:
Implement a function named `pandas_to_numpy` that takes a pandas DataFrame `df` as input and returns its equivalent NumPy array. The function should handle DataFrames of any size, different data types, and missing values (NaN). It should not use any built-in functions for conversion, such as pandas' `to_numpy()` or `values` attribute. The function should be optimized for efficiency and avoid unnecessary computations or memory usage.
"""

import numpy as np
import pandas as pd

def pandas_to_numpy(df):
    # Get the shape of the DataFrame
    num_rows, num_cols = df.shape
    
    # Initialize an empty NumPy array of the same shape as the DataFrame
    array = np.empty((num_rows, num_cols), dtype=object)
    
    # Iterate over the DataFrame and copy the values to the NumPy array
    for i in range(num_rows):
        for j in range(num_cols):
            value = df.iat[i, j]  # Get the value at the current position
            if pd.isnull(value):
                array[i, j] = np.nan  # Convert NaN to NumPy's NaN
            else:
                array[i, j] = value  # Copy the value to the array
    
    return array