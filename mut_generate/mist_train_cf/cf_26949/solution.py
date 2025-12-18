"""
QUESTION:
You are given an array of integers representing stock prices on different days. Write a function `maxProfit(prices: List[int]) -> int` that returns the maximum possible profit from buying and selling a single stock, considering that you can only hold one stock at a time and must sell before buying again. If no profit can be made, return 0.
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