"""
QUESTION:
Write a function named `calculate_strike_price` that calculates the strike price for an ATM DNS (Delta Neutral Straddle) option using the formula S0 * e^((r+0.5*sigma^2)T), where S0 is the initial stock price, r is the risk-free interest rate, sigma is the volatility, and T is the time to expiration. The function should take in the initial stock price, risk-free interest rate, volatility, and time to expiration as inputs, and return the calculated strike price.
"""

import math

def calculate_strike_price(S0, r, sigma, T):
    """
    Calculate the strike price for an ATM DNS (Delta Neutral Straddle) option.

    Args:
    S0 (float): The initial stock price.
    r (float): The risk-free interest rate.
    sigma (float): The volatility.
    T (float): The time to expiration.

    Returns:
    float: The calculated strike price.
    """
    return S0 * math.exp((r + 0.5 * sigma ** 2) * T)