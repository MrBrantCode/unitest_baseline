"""
QUESTION:
Develop a function named `max_profit` that calculates the maximum possible profit from buying and selling stocks given a list of daily stock prices. The stock must be bought before it can be sold, and the function should handle cases where no profit is possible. The function should take a list of integers representing the daily stock prices as input and return an integer representing the maximum possible profit.
"""

def max_profit(stock_prices):
    # initialize minimum price as the first stock price
    min_price = stock_prices[0]
    # initialize max profit as 0
    max_profit = 0

    # iterate over the entire list of stock prices
    for price in stock_prices:
        # if current price is less than minimum price, update minimum price
        if price < min_price:
            min_price = price
        # if current price - minimum price > max profit then update max profit
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit