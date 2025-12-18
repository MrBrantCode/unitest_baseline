"""
QUESTION:
Calculate the Sharpe ratio for a long-short portfolio given the daily returns for both long and short positions. Implement a function `calculate_sharpe_ratio` that takes in two parameters: `long_returns` and `short_returns`, both of which are lists of daily returns. The function should return a tuple containing the daily Sharpe ratio and the annualized Sharpe ratio. Assume there are 252 trading days in a year. Do not consider transaction costs in the calculation.
"""

import numpy as np
from math import sqrt

def calculate_sharpe_ratio(long_returns, short_returns):
    """
    Calculate the daily and annualized Sharpe ratio for a long-short portfolio.

    Args:
        long_returns (list): A list of daily returns for the long positions.
        short_returns (list): A list of daily returns for the short positions.

    Returns:
        tuple: A tuple containing the daily Sharpe ratio and the annualized Sharpe ratio.
    """
    # Calculate the net returns for the portfolio
    net_returns = np.array(long_returns) - np.array(short_returns)
    
    # Calculate the daily Sharpe ratio
    daily_sharpe_ratio = np.mean(net_returns) / np.std(net_returns)
    
    # Calculate the annualized Sharpe ratio
    annualized_sharpe_ratio = daily_sharpe_ratio * sqrt(252)
    
    return daily_sharpe_ratio, annualized_sharpe_ratio