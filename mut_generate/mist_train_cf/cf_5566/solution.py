"""
QUESTION:
Write a function `sum_dataframe_elements` that calculates the sum of all elements in a pandas DataFrame. The function should be able to handle DataFrames containing both numeric and non-numeric values.
"""

import pandas as pd
import numpy as np

def sum_dataframe_elements(df):
    """
    Calculate the sum of all elements in a pandas DataFrame.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame containing numeric values.
    
    Returns:
    float: The sum of all numeric elements in the DataFrame.
    """
    return df.select_dtypes(include=[np.number]).values.sum()