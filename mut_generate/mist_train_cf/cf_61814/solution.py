"""
QUESTION:
Create a function `replace_nan_with_mean` that takes a pandas DataFrame as input. The function should replace any NaN values in the numeric columns of the DataFrame with the mean value of their respective columns. The function should not affect non-numeric columns.
"""

import pandas as pd
import numpy as np

def replace_nan_with_mean(df):
    """
    Replace NaN values in numeric columns of a pandas DataFrame with their respective mean values.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with NaN values in numeric columns replaced.
    """

    # Replace NaN values with the mean value of their respective numeric columns
    df = df.apply(lambda x: x.fillna(x.mean()) if x.dtype in ['int64', 'float64'] else x)
    
    return df