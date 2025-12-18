"""
QUESTION:
Write a function `convert_to_hours` that takes a pandas DataFrame `df` with two columns 'coupon' and 'expiration', where 'expiration' contains strings representing time in 'days' or 'hours' (e.g., '1d', '2h'). Convert the 'expiration' column to hours and return the updated DataFrame. The function should work with pandas version 0.25.0 or later.
"""

import pandas as pd

def convert_to_hours(df):
    """
    Convert the 'expiration' column in the DataFrame from 'days' or 'hours' to hours.

    Parameters:
    df (pandas DataFrame): A DataFrame with two columns 'coupon' and 'expiration'.

    Returns:
    pandas DataFrame: The updated DataFrame with 'expiration' column converted to hours.
    """
    df['expiration'] = pd.to_timedelta(df['expiration'])
    df['expiration'] = df['expiration'].dt.total_seconds() / 3600
    return df