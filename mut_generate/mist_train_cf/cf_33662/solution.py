"""
QUESTION:
Given a list of integers representing daily stock prices, write a function `count_increasing_days` that takes this list as input and returns the number of "increasing" days, where the stock price is higher than the previous day's price. The input list is not empty and contains at least two elements. The function should return 0 if no increasing days are found.
"""

def entance(stock_prices):
    increasing_count = 0
    for i in range(1, len(stock_prices)):
        if stock_prices[i] > stock_prices[i - 1]:
            increasing_count += 1
    return increasing_count