"""
QUESTION:
Design a function `calculate_max_profit` to find the maximum possible profit from buying and selling one share of stock, given a list of daily share prices. The function should return the maximum possible profit. The share can only be bought and sold once.
"""

def calculate_max_profit(prices):
    """
    Calculate the maximum possible profit from buying and selling one share of stock.

    Args:
    prices (list): A list of daily share prices.

    Returns:
    int: The maximum possible profit.
    """
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        # Update the minimum price if a lower price is found
        if price < min_price:
            min_price = price
        # Update the maximum profit if a higher profit is found
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit