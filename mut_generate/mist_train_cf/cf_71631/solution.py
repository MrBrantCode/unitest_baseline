"""
QUESTION:
Estimate the daily volatility of an asset given its high, low, open, and close prices using the Parkinson volatility estimator. The function should take in a pandas Series or DataFrame with 'High' and 'Low' columns and return the estimated volatility. The volatility should be calculated using the formula: 0.199 * sqrt((1/(4*ln(2)))*[ln(High ÷ Low)²]).

The function should be named `parkinson_volatility` and it should return a pandas Series of the estimated volatility for each day.
"""

import pandas as pd
import numpy as np

def parkinson_volatility(df):
    """
    Estimates daily volatility of an asset given its high, low, open, and close prices 
    using the Parkinson volatility estimator.

    Parameters:
    df (pd.DataFrame): A DataFrame with 'High' and 'Low' columns.

    Returns:
    pd.Series: A Series of the estimated volatility for each day.
    """
    return 0.199 * np.sqrt((1/(4*np.log(2)))*(np.log(df['High'] / df['Low'])**2))