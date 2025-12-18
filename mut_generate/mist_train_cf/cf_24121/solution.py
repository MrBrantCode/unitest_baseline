"""
QUESTION:
Write a function `calculate_average_price` that takes a list of prices as input and returns the average price. The function must use list comprehension to calculate the sum of prices. The input list contains decimal numbers and may not be empty.
"""

def calculate_average_price(prices):
    """
    Calculate the average price from a list of prices.

    Args:
        prices (list): A list of decimal numbers representing prices.

    Returns:
        float: The average price.
    """
    return sum([price for price in prices]) / len(prices)