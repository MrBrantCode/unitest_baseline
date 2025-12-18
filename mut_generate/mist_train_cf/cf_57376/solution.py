"""
QUESTION:
Write a function called `compare_gammas` that calculates and compares the Gamma of an American put option and its European counterpart. The function should take in parameters such as the underlying price, time to expiry, volatility, interest rate, and dividend yield, and return whether the American put Gamma is necessarily greater than or equal to that of the European counterpart.
"""

import math

def compare_gammas(S, T, r, sigma, q):
    """
    Calculate the Gamma of a European put option using the Black-Scholes model.
    
    Parameters:
    S (float): Underlying price
    T (float): Time to expiry
    r (float): Interest rate
    sigma (float): Volatility
    q (float): Dividend yield
    
    Returns:
    float: Gamma of the European put option
    """
    
    # Calculate d1
    d1 = (math.log(S / 100) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    
    # Calculate Gamma using the formula for European put option
    gamma = math.exp(-q * T) * math.exp(-(d1 ** 2) / 2) / (S * sigma * math.sqrt(2 * math.pi * T))
    
    return gamma