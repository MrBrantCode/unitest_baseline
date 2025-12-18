"""
QUESTION:
Create a function `max_profit(stock_prices)` that calculates the maximum possible profit from buying and selling stocks given a list of non-negative stock prices over time. The function should assume that buying and selling on the same day is not allowed.
"""

def max_profit(stock_prices):
    """
    Calculate the maximum possible profit from buying and selling stocks given a list of non-negative stock prices over time.

    Args:
    stock_prices (list): A list of non-negative stock prices over time.

    Returns:
    int: The maximum possible profit.
    """
    min_price = stock_prices[0]
    max_profit = 0
    
    for price in stock_prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
        
    return max_profit