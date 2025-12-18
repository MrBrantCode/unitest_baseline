"""
QUESTION:
Write a function `max_buns` that calculates the maximum whole number of buns that can be purchased with a given amount of money. The function should take two parameters: `bun_price` (the price of each bun) and `money` (the amount of money available). The function should return the maximum number of buns that can be purchased without exceeding the available money.
"""

def max_buns(bun_price, money):
    """
    Calculate the maximum whole number of buns that can be purchased with a given amount of money.

    Args:
        bun_price (float): The price of each bun.
        money (float): The amount of money available.

    Returns:
        int: The maximum number of buns that can be purchased without exceeding the available money.
    """
    return money // bun_price