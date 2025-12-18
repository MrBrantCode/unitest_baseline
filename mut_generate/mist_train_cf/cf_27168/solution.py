"""
QUESTION:
You are given an array `prices` where `prices[i]` is the stock price on the `i`-th day. Write a function `maxProfit(prices)` to find the maximum profit achievable from buying and selling the stock at most once. The function should take the array of stock prices as input and return the maximum achievable profit.
"""

def maxProfit(prices):
    minBuy = float('inf')  
    maxProfits = 0
    
    for price in prices:
        minBuy = min(minBuy, price)  
        maxProfits = max(maxProfits, price - minBuy)  
        
    return maxProfits