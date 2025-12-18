"""
QUESTION:
Create a function called `calculate_interval_size` that takes three parameters: `low_price`, `high_price`, and `num_intervals`. The function should calculate the percentage gap between each interval, where the intervals are distributed logarithmically (binomially) between the `low_price` and `high_price`. The intervals should have the same percentage change. The function should return the interval size, which is the ratio between successive price levels.
"""

import math

def calculate_interval_size(low_price, high_price, num_intervals):
    """
    Calculate the interval size for logarithmically distributed price levels.
    
    Parameters:
    low_price (float): The low price
    high_price (float): The high price
    num_intervals (int): The number of intervals
    
    Returns:
    float: The interval size, which is the ratio between successive price levels
    """
    ratio = high_price / low_price
    interval_size = math.pow(ratio, 1.0 / num_intervals)
    return interval_size