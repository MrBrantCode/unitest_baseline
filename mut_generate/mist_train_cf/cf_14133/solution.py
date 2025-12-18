"""
QUESTION:
Create a function named `normalize_dataframe` that takes a pandas DataFrame as input and returns a new DataFrame with all values scaled between 0 and 1 and rounded to the nearest two decimal places. The function should not modify the original DataFrame. The scaling should be performed column-wise, with each column scaled separately based on its minimum and maximum values.
"""

import pandas as pd

def normalize_dataframe(df):
    # Calculate the minimum and maximum values for each column
    min_values = df.min()
    max_values = df.max()
    
    # Normalize the dataframe by scaling values between 0 and 1
    normalized_df = (df - min_values) / (max_values - min_values)
    
    # Round the values to the nearest two decimal places
    normalized_df = normalized_df.round(2)
    
    return normalized_df