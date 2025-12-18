"""
QUESTION:
Write a function `calculate_acf_from_pacf` that takes a list of PACF values at lags 1, 2, and 3 as input and returns the corresponding ACF values at lags 1, 2, and 3. Assume that the PACF values are calculated using the Yule-Walker Equations and the input list contains the PACF values in the order of lag 1, 2, and 3.
"""

import numpy as np

def calculate_acf_from_pacf(pacf_values):
    """
    Calculate ACF values at lags 1, 2, and 3 from PACF values using Yule-Walker Equations.

    Parameters:
    pacf_values (list): A list of PACF values at lags 1, 2, and 3.

    Returns:
    list: A list of ACF values at lags 1, 2, and 3.
    """
    # Initialize ACF values
    acf_values = [pacf_values[0]]  # ACF at lag 1 is the same as PACF at lag 1
    
    # Calculate ACF at lag 2
    acf_values.append(pacf_values[1] + pacf_values[0] * acf_values[0])
    
    # Calculate ACF at lag 3
    acf_values.append(pacf_values[2] + pacf_values[1] * acf_values[0] + pacf_values[0] * acf_values[1])
    
    return acf_values