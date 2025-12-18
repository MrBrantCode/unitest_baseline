"""
QUESTION:
Design a function `maxProfit` that calculates the maximum possible profit from multiple transactions of buying and selling a company's stock. The function should take an array of stock prices as input and return the maximum profit, with the constraint that you cannot engage in simultaneous transactions (i.e., you must sell the stock before buying again). The stock prices may fluctuate, including decreases in value.
"""

def maxProfit(prices):
    """
    Calculate the maximum possible profit from multiple transactions of buying and selling a company's stock.

    Args:
        prices (list): A list of stock prices.

    Returns:
        int: The maximum profit.
    """
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i+1] > prices[i]:
            profit += prices[i+1] - prices[i]
    return profit