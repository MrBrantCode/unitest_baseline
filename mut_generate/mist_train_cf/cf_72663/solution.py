"""
QUESTION:
Write a function `calculate_stress_var` that estimates the potential loss that a bank or financial institution might face under stressed market conditions, also known as Stress Value at Risk (SVaR). The function should take as input a time series of portfolio returns and a specific stress period, and return the SVaR value. The stress period should be a specific time range, such as the 2008-2009 financial crisis, and the function should use a rolling window of 251 days to estimate the SVaR. The output should be the fifth percentile worst return, representing the VaR99%.
"""

import numpy as np

def calculate_stress_var(portfolio_returns, stress_period):
    """
    Estimates the potential loss that a bank or financial institution might face 
    under stressed market conditions, also known as Stress Value at Risk (SVaR).

    Args:
        portfolio_returns (array-like): Time series of portfolio returns.
        stress_period (array-like): Specific time range, such as the 2008-2009 financial crisis.

    Returns:
        float: The fifth percentile worst return, representing the VaR99%.
    """
    # Filter portfolio returns for the stress period
    stress_returns = [return_val for return_val, period in zip(portfolio_returns, stress_period) if period]

    # Calculate rolling 251-day window
    stress_var = np.percentile(stress_returns, 5)

    return stress_var