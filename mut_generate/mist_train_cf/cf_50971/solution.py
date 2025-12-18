"""
QUESTION:
Calculate the volatility of a spread given the historical volatilities and correlation of its components. The spread consists of two 2-year treasuries and one 10-year treasury. 

Write a function `calculate_spread_volatility` that takes as input the historical volatilities of the 2-year and 10-year treasuries, the quantities of each treasury in the spread, and the correlation between the returns of the two treasuries. The function should return the volatility of the spread.
"""

import math

def calculate_spread_volatility(short_volatility, long_volatility, short_quantity, long_quantity, correlation):
    """
    Calculate the volatility of a spread given the historical volatilities and correlation of its components.

    Args:
    short_volatility (float): Historical volatility of the short-term treasury.
    long_volatility (float): Historical volatility of the long-term treasury.
    short_quantity (int): Quantity of short-term treasuries in the spread.
    long_quantity (int): Quantity of long-term treasuries in the spread.
    correlation (float): Correlation between the returns of the two treasuries.

    Returns:
    float: Volatility of the spread.
    """
    # Calculate the variance of the spread using the formula for the variance of a portfolio
    variance = (short_quantity ** 2) * (short_volatility ** 2) + (long_quantity ** 2) * (long_volatility ** 2) + 2 * short_quantity * long_quantity * short_volatility * long_volatility * correlation
    
    # Calculate the volatility of the spread by taking the square root of the variance
    volatility = math.sqrt(variance)
    
    return volatility