"""
QUESTION:
Create a function called `find_fair_price_parameter` that calculates the value of a parameter in a trinomial model to obtain a "fair price" of a European-type option, considering the underlying asset's expected return, risk-free rate, volatility, and time to maturity.
"""

def find_fair_price_parameter(S, K, T, r, sigma, u, d, q, type):
    """
    Calculate the value of a parameter in a trinomial model to obtain a "fair price" of a European-type option.

    Parameters:
    S (float): Current stock price
    K (float): Strike price
    T (float): Time to maturity (in years)
    r (float): Risk-free interest rate
    sigma (float): Volatility of the underlying asset
    u (float): Up factor
    d (float): Down factor
    q (float): Probability of an upward movement
    type (str): Type of option ('call' or 'put')

    Returns:
    float: Fair price of the option
    """
    import math
    # calculate probability of upward movement
    p = (math.exp(r*T) - d) / (u - d)

    if type == 'call':
        return max(S * (u**2) * q**2 + S * u * d * 2 * q * (1-q) + S * d**2 * (1-q)**2 - K * (u**2) * q**2 * math.exp(-r*T) - K * u * d * 2 * q * (1-q) * math.exp(-r*T) - K * d**2 * (1-q)**2 * math.exp(-r*T), 0)
    elif type == 'put':
        return max(K * (u**2) * q**2 * math.exp(-r*T) + K * u * d * 2 * q * (1-q) * math.exp(-r*T) + K * d**2 * (1-q)**2 * math.exp(-r*T) - S * (u**2) * q**2 - S * u * d * 2 * q * (1-q) - S * d**2 * (1-q)**2, 0)
    else:
        return "Invalid option type"