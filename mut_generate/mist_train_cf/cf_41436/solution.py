"""
QUESTION:
Create a function named `get_average_price` within the `Stock` class that calculates the average stock price over a specified time period given a `start_date` and an `end_date`. The function should accept `start_date` and `end_date` as strings in the 'YYYY-MM-DD' format and return the average stock price as a float.
"""

def get_average_price(prices):
    """
    Calculate the average stock price given a list of prices.

    Args:
        prices (list): A list of stock prices.

    Returns:
        float: The average stock price.
    """
    return sum(prices) / len(prices)