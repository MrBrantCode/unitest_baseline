"""
QUESTION:
Write a function called `calculate_varswap_value` that calculates the value of a varswap given the stochastic nature of interest rates. Use a rates model such as Vasicek's model or the Cox-Ingersoll-Ross (CIR) model to represent the interest rates, and consider the timeframe of the varswap when deciding whether to account for stochastic interest rates.
"""

import numpy as np

def calculate_varswap_value(S, r, T, K, sigma, kappa, theta, v0):
    """
    Calculate the value of a varswap using the CIR model for stochastic interest rates.

    Args:
    S (float): The current price of the underlying asset.
    r (float): The current interest rate.
    T (float): The time to maturity of the varswap in years.
    K (float): The strike price of the varswap.
    sigma (float): The volatility of the underlying asset.
    kappa (float): The mean reversion parameter of the CIR model.
    theta (float): The long-term mean of the CIR model.
    v0 (float): The initial variance of the CIR model.

    Returns:
    float: The value of the varswap.
    """

    # Calculate the expected value of the variance using the CIR model
    expected_variance = (theta / kappa) * (1 - np.exp(-kappa * T)) + v0 * np.exp(-kappa * T)

    # Calculate the value of the varswap
    varswap_value = (expected_variance - K) * T

    return varswap_value