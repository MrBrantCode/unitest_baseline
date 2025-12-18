"""
QUESTION:
Write a function `calculate_vrp` that takes as input the implied volatility of the front-quarter option and the annualized future realized volatility until the expiration of the front-option contract. The function should return the Volatility Risk Premium (VRP), which is the difference between the implied volatility and the realized volatility.
"""

def calculate_vrp(implied_volatility, realized_volatility):
    """
    Calculate the Volatility Risk Premium (VRP) as the difference between 
    the implied volatility and the realized volatility.

    Args:
    - implied_volatility (float): The implied volatility of the front-quarter option.
    - realized_volatility (float): The annualized future realized volatility until 
                                   the expiration of the front-option contract.

    Returns:
    - float: The Volatility Risk Premium.
    """
    return implied_volatility - realized_volatility