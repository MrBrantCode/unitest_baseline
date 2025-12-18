"""
QUESTION:
Write a function called `calculate_average_price` that takes a list of prices as input and returns the average price. The function should handle any number of prices and should not take any other arguments.
"""

def calculate_average_price(prices):
    """
    Calculate the average price from a list of prices.

    Args:
        prices (list): A list of prices.

    Returns:
        float: The average price.
    """
    return sum(prices) / len(prices)