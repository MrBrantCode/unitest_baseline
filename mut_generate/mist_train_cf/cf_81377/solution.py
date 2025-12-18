"""
QUESTION:
Given a European volatility surface of an asset, implement a function named `price_american_option` to calculate the theoretical price of an American option, taking into account the underlying asset price, strike price, risk-free interest rate, time to expiration, and volatility. The function should use a binomial lattice model and backward induction to compute the option price.
"""

import numpy as np

def price_american_option(S, K, T, r, sigma, n=100, option_type='call'):
    """
    Calculate the theoretical price of an American option using a binomial lattice model.

    Parameters:
    S (float): Underlying asset price
    K (float): Strike price
    T (float): Time to expiration in years
    r (float): Risk-free interest rate
    sigma (float): Volatility
    n (int): Number of steps in the binomial lattice
    option_type (str): Type of option ('call' or 'put')

    Returns:
    float: Theoretical price of the American option
    """

    # Calculate time step
    dt = T / n
    
    # Calculate up and down factors
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    
    # Calculate risk-neutral probabilities
    p = (np.exp(r * dt) - d) / (u - d)
    
    # Initialize the lattice with zeros
    lattice = np.zeros((n + 1, n + 1))
    
    # Calculate terminal payoffs
    for i in range(n + 1):
        if option_type == 'call':
            lattice[i, n] = max(0, S * (u ** (n - i)) * (d ** i) - K)
        elif option_type == 'put':
            lattice[i, n] = max(0, K - S * (u ** (n - i)) * (d ** i))
    
    # Backward induction
    for j in range(n - 1, -1, -1):
        for i in range(j + 1):
            lattice[i, j] = max(
                (option_type == 'call' and (S * (u ** (j - i)) * (d ** i) - K)) or 
                (option_type == 'put' and (K - S * (u ** (j - i)) * (d ** i))), 
                np.exp(-r * dt) * (p * lattice[i, j + 1] + (1 - p) * lattice[i + 1, j + 1])
            )
    
    return lattice[0, 0]