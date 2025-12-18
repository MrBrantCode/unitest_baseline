"""
QUESTION:
Design a function `maximumProfit` that calculates the maximum possible profit obtainable from a sequence of day-to-day stock market prices, given a limit to the number of allowable trades. The function should accept two parameters: a list of stock prices (`stock_prices`) and the limit to the number of trades (`trade_limit`). It should return the maximum profit achievable given these parameters, taking into account that buying must occur before selling and that excessive trading is penalized.
"""

def maximumProfit(stock_prices, trade_limit):
    if not stock_prices or trade_limit == 0:
        return 0

    profit = 0
    buy = stock_prices[0]
    sell = stock_prices[0]
    trade_count = 0

    for i in range(1, len(stock_prices)):
        if stock_prices[i] < sell:
            if trade_count < trade_limit:
                profit += sell - buy
                trade_count += 1
            buy = stock_prices[i]
            sell = stock_prices[i]
        elif stock_prices[i] > sell:
            sell = stock_prices[i]

    if trade_count < trade_limit:
        profit += sell - buy

    return profit