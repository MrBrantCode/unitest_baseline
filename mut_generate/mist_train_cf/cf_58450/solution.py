"""
QUESTION:
Write a function `max_profit(stock_prices)` that calculates the maximum possible profit from buying and selling stocks given a list of daily stock prices. The function should return 0 if it is not possible to make a profit. The stock must be bought before it is sold.
"""

def max_profit(stock_prices):
    if len(stock_prices) < 2:
        return 0

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for price in stock_prices[1:]:
        profit = price - min_price
        max_profit = max(profit, max_profit)
        min_price = min(price, min_price)

    return max_profit if max_profit > 0 else 0