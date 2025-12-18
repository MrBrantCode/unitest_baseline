"""
QUESTION:
Write a function named `sharpe_ratio` that calculates the Sharpe ratio given the return rates and the risk-free rate. The function should use the mean of the return rates and the standard deviation of the return rates in its calculation.
"""

import numpy as np

def sharpe_ratio(returns, risk_free_rate):
    """
    Calculate the Sharpe ratio given the return rates and the risk-free rate.

    Args:
    - returns (list): A list of return rates
    - risk_free_rate (float): The risk-free rate

    Returns:
    - sharpe_ratio (float): The Sharpe ratio
    """
    mean_returns = np.mean(returns)
    std_dev_returns = np.std(returns)
    sharpe_ratio = (mean_returns - risk_free_rate) / std_dev_returns
    return sharpe_ratio