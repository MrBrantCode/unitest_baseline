"""
QUESTION:
Create a function named `maxProfit` that calculates the maximum possible profit from a list of stock prices. The function should take a list of integers representing the stock prices for each day and return an integer representing the maximum possible profit. The function should assume that a stock can only be sold after it has been bought and that buying and selling on the same day is not allowed. The function should have a time complexity of O(n), where n is the number of days.
"""

def maxProfit(prices):
    min_price, max_profit = float('inf'), 0
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit