"""
QUESTION:
Implement a function `maxProfit` that takes in an array of stock prices, where each index represents a day and the value represents the price of the stock on that day, and returns the maximum profit that can be achieved by buying and selling the stock once. The function should have a time complexity of O(n), where n is the number of stock prices in the input array.
"""

def maxProfit(prices):
    if not prices:
        return 0
    
    max_profit = 0
    min_price = prices[0]
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    
    return max_profit