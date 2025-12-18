"""
QUESTION:
Create a function `replace_nan_values` that takes a pandas DataFrame as input. The function should replace NaN values in numerical columns with the median value of their respective columns and in categorical columns with the mode (most frequent) value of their respective columns. The function should handle missing values in a way that minimizes the need for looping over data to optimize performance for large datasets.
"""

import pandas as pd
import numpy as np

def replace_nan_values(df):
    """
    Replace NaN values in numerical columns with the median value of their respective columns 
    and in categorical columns with the mode (most frequent) value of their respective columns.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: The DataFrame with NaN values replaced.
    """
    # First identify numeric and categorical columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=[object]).columns

    # Replacing NaN values in numeric columns with the median
    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)
        
    # Replacing NaN values in categorical columns with the mode
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

    return df