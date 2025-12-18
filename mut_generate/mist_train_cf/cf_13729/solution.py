"""
QUESTION:
Design a function `max_profit` that calculates the maximum possible profit from buying and selling a company's stock any number of times, given an array of share prices. The function must only consider one transaction at a time, selling shares before buying again. The function should have a time complexity of O(n), where n is the number of share prices, and a space complexity of O(1).
"""

def max_profit(prices):
    """
    Calculate the maximum possible profit from buying and selling a company's stock any number of times.

    Args:
    prices (list): A list of share prices.

    Returns:
    int: The maximum possible profit.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    current_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > current_profit:
            current_profit = price - min_price
            max_profit += current_profit
            min_price = price
    
    return max_profit