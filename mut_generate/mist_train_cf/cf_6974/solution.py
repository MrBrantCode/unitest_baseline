"""
QUESTION:
Design a function `maxProfit` that calculates the maximum possible profit from buying and selling a stock at most twice, with an optional transaction fee. The function should take an array of stock prices and a transaction fee as input, and return the maximum possible profit.

The function should have a time complexity of O(n), where n is the length of the stock prices array, and a space complexity of O(1). If a transaction fee is provided, it should be subtracted from the profit for each buy/sell action.
"""

def maxProfit(prices, fee):
    """
    Calculate the maximum possible profit from buying and selling a stock at most twice, 
    with an optional transaction fee.

    Args:
    prices (list): A list of stock prices.
    fee (int): The transaction fee.

    Returns:
    int: The maximum possible profit.
    """
    buy1 = float('inf')
    buy2 = float('inf')
    sell1 = 0
    sell2 = 0

    for price in prices:
        buy1 = min(buy1, price)
        sell1 = max(sell1, price - buy1 - fee)
        buy2 = min(buy2, price - sell1 - fee)
        sell2 = max(sell2, price - buy2 - fee)

    return sell2