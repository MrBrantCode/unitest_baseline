"""
QUESTION:
Write a function `max_profit(prices)` that finds the maximum possible profit from a list of daily stock prices `prices` by buying and selling at most once. The function should return 0 if no profit can be made. The input `prices` is a list of integers and the function should solve the problem in an efficient manner.
"""

def entance(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    
    return max_profit