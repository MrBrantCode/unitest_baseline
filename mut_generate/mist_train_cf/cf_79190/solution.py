"""
QUESTION:
Given the array `prices` where `prices[i]` represents the cost of a stock on the `i-th` day, write a function `maxProfit(prices)` to determine the maximum possible profit that can be obtained with at most two transactions. The function should not allow simultaneous transactions, i.e., you must sell the stock before you can purchase it again. The constraints are `1 <= prices.length <= 10^5` and `0 <= prices[i] <= 10^5`.
"""

def maxProfit(prices):
    if len(prices) < 2: return 0
    
    first_buy, first_sell = float('-inf'), 0
    second_buy, second_sell = float('-inf'), 0
    for p in prices:
        first_buy = max(first_buy, -p)
        first_sell = max(first_sell, first_buy + p)
        second_buy = max(second_buy, first_sell - p)
        second_sell = max(second_sell, second_buy + p)
    
    return second_sell