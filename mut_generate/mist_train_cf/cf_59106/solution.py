"""
QUESTION:
Write a function `handle_option_data` to clean and handle option data for Heston model calibration. The function should take a pandas DataFrame `df` containing option data as input and return a cleaned DataFrame. The DataFrame should have columns 'strike', 'maturity', 'trade_volume', 'open_interest', 'ITM_OTM', and 'time_to_maturity'. Assume the interest rate and dividend data are already accounted for in the option pricing model. The function should apply the following data handling rules: remove options with no trade/volume, remove outliers, handle ITM/OTM options, select a suitable number of maturities, apply interpolation if necessary, and exclude options with near maturities.
"""

import pandas as pd
import numpy as np

def handle_option_data(df):
    """
    Clean and handle option data for Heston model calibration.

    Parameters:
    df (pd.DataFrame): A pandas DataFrame containing option data.
    The DataFrame should have columns 'strike', 'maturity', 'trade_volume', 'open_interest', 'ITM_OTM', and 'time_to_maturity'.

    Returns:
    pd.DataFrame: A cleaned DataFrame.
    """
    
    # Remove options with no trade/volume
    df = df[(df['trade_volume'] > 0) & (df['open_interest'] > 0)]
    
    # Remove outliers
    df = df[(np.abs(df['strike'] - df['strike'].mean()) <= (3 * df['strike'].std()))]
    
    # Handle ITM/OTM options
    df = pd.get_dummies(df, columns=['ITM_OTM'])
    
    # Select a suitable number of maturities
    # For demonstration purposes, let's assume we want to select 3 maturities
    df['maturity'] = pd.qcut(df['maturity'], 3, labels=False)
    
    # Apply interpolation if necessary
    # For demonstration purposes, let's assume we want to interpolate missing values in the 'strike' column
    df['strike'] = df['strike'].interpolate(method='linear', limit_direction='both')
    
    # Exclude options with near maturities
    # For demonstration purposes, let's assume we want to exclude options with a time to maturity less than 1 week
    df = df[df['time_to_maturity'] >= 7]
    
    return df