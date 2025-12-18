"""
QUESTION:
You are given an array `prices` of stock prices and a non-negative integer `fee` representing a transaction fee. Write a function `maxProfit(prices, fee)` that returns the maximum profit achievable by buying and selling the stock multiple times while paying the transaction fee for each transaction, with the restriction that you cannot engage in multiple transactions simultaneously. The function should take a list of integers `prices` (1 <= len(prices) <= 5 * 10^4, 1 <= prices[i] <= 10^5) and a non-negative integer `fee` (0 <= fee <= 5 * 10^4) as input.
"""

def maxProfit(prices, fee):
    """
    Returns the maximum profit achievable by buying and selling the stock multiple times 
    while paying the transaction fee for each transaction.

    Args:
    prices (List[int]): A list of stock prices.
    fee (int): A non-negative integer representing a transaction fee.

    Returns:
    int: The maximum profit achievable.
    """
    result = 0
    lo = float('inf')

    for price in prices:
        if price < lo:
            lo = price
        else:
            profit = price - lo - fee
            if profit > 0:
                result += profit
                lo = price - fee  
    return result