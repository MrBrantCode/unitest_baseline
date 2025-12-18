"""
QUESTION:
Write a function `maxProfit` that takes an array of integers `prices` as input and returns the maximum possible profit that can be achieved by buying and selling the stock at most once. The function should have a time complexity of O(n), where n is the number of elements in `prices`. Assume that buying and selling on the same day is not allowed and the function should return 0 if the input array is empty.
"""

def maxProfit(prices):
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