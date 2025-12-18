"""
QUESTION:
Write a function `max_profit(prices, fee)` that calculates the maximum possible revenue from buying and selling shares given a sequence of daily share prices and a transaction fee. The function must ensure that a share is purchased before it is sold and does not allow selling on the same day as purchasing.
"""

def max_profit(prices, fee):
    n = len(prices)
    if n < 2:
        return 0
    buy, sell = [0]*n, [0]*n
    buy[0] = -prices[0] - fee
    for i in range(1, n):
        if i == 1:
            buy[i] = max(buy[i-1], -prices[i]-fee)
        else:
            buy[i] = max(buy[i-1], sell[i-2]-prices[i]-fee)
        sell[i] = max(sell[i-1], buy[i-1]+prices[i]-fee)
    return max(sell)