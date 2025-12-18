"""
QUESTION:
Write a function `calculate_expected_loss` that calculates the expected loss of a stock return given its volatility, assuming it follows a normal distribution. The expected loss is the expected value of the negative returns, which can be approximated using the mean of a half-normal distribution. The mean of a half-normal distribution is given by sigma * sqrt(2 / pi), where sigma is the standard deviation of the normal distribution. The function should return the expected loss as a percentage.
"""

import math

def calculate_expected_loss(volatility):
    """
    Calculate the expected loss of a stock return given its volatility.
    
    Parameters:
    volatility (float): The standard deviation of the normal distribution.
    
    Returns:
    float: The expected loss as a percentage.
    """
    return -volatility * math.sqrt(2 / math.pi)