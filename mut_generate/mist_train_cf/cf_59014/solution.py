"""
QUESTION:
Develop a function named `update_status` that takes a pandas DataFrame as input and updates the 'Status' column based on the 'Age' column values. If the 'Age' is greater than 30, set 'Status' to 'Old', otherwise set it to 'Young'.
"""

import pandas as pd

def update_status(df):
    """
    Updates the 'Status' column in the input DataFrame based on the 'Age' column values.
    
    Parameters:
    df (pandas DataFrame): DataFrame containing 'Age' and 'Status' columns.
    
    Returns:
    pandas DataFrame: The input DataFrame with the 'Status' column updated.
    """
    df['Status'] = df['Age'].apply(lambda x: 'Old' if x > 30 else 'Young')
    return df