"""
QUESTION:
Write a function called `max_stock_profit` that takes a list of stock prices as input and returns the maximum possible profit that can be obtained by buying and selling the stock once. The function should assume that the list of stock prices is not empty and contains only positive numbers, and that the stock can be sold on the same day it is bought. The function should also assume that the stock can only be bought and sold once.
"""

def max_stock_profit(prices):
    """
    This function calculates the maximum possible profit that can be obtained by buying and selling the stock once.

    Args:
    prices (list): A list of stock prices.

    Returns:
    int: The maximum possible profit.
    """
    # Initialize variables
    min_price = float('inf')
    max_profit = 0
    
    # Loop through each day and calculate the maximum profit
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
                
    # Return the maximum profit
    return max_profit