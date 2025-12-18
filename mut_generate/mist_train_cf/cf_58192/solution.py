"""
QUESTION:
Write a function `information_ratio` that takes as input a portfolio's returns and a benchmark's returns, and returns the Information Ratio (IR) as a measure of a portfolio manager's ability to generate excess returns relative to a benchmark, given the amount of risk taken. Assume that the input arrays have the same length, representing returns over the same time period, and that the risk is measured by the standard deviation of the portfolio's returns relative to the benchmark's returns.
"""

import numpy as np

def information_ratio(portfolio_returns, benchmark_returns):
    """
    Calculate the Information Ratio (IR) as a measure of a portfolio manager's ability to generate excess returns relative to a benchmark.

    Args:
    portfolio_returns (array): The returns of the portfolio.
    benchmark_returns (array): The returns of the benchmark.

    Returns:
    float: The Information Ratio (IR) of the portfolio.
    """
    excess_returns = portfolio_returns - benchmark_returns
    tracking_error = np.std(excess_returns)
    information_ratio = np.mean(excess_returns) / tracking_error
    return information_ratio