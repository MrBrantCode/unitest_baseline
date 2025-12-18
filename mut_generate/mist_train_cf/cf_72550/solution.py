"""
QUESTION:
Write a function `calculate_gsd` that takes a list of returns as input and returns the geometric standard deviation (GSD). The GSD should be calculated by taking the exponent of the standard deviation of the logarithmic returns.
"""

import numpy as np

def calculate_gsd(returns):
    """
    Calculate the geometric standard deviation (GSD) of a list of returns.

    Args:
        returns (list): A list of returns.

    Returns:
        float: The geometric standard deviation.
    """
    log_returns = np.log(returns)
    std_dev = np.std(log_returns)
    gsd = np.exp(std_dev)
    return gsd