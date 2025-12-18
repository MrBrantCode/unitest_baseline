"""
QUESTION:
Calculate the function `calculate_volatility` that estimates annual volatility from a list of asset prices at inconsistent time intervals. The function should take two lists as input: `prices` and `intervals`, where `prices` is a list of asset prices and `intervals` is a list of time intervals corresponding to each price. The function should return the estimated annual volatility.
"""

import math

def calculate_volatility(prices, intervals):
    """
    Estimates annual volatility from a list of asset prices at inconsistent time intervals.

    Args:
        prices (list): A list of asset prices.
        intervals (list): A list of time intervals corresponding to each price.

    Returns:
        float: The estimated annual volatility.
    """
    # Calculate the adjusted log returns
    log_returns = []
    for i in range(1, len(prices)):
        n = intervals[i]
        log_return = math.log(prices[i] / prices[i-1]) / math.sqrt(n)
        log_returns.append(log_return)

    # Calculate the standard deviation (volatility) of the adjusted log returns
    mean_return = sum(log_returns) / len(log_returns)
    variance = sum((x - mean_return) ** 2 for x in log_returns) / len(log_returns)
    volatility = math.sqrt(variance) * math.sqrt(252)  # 252 trading days in a year

    return volatility