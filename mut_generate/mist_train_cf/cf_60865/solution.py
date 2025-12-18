"""
QUESTION:
Write a function `maxProfit(prices, fee)` that calculates the maximum possible profit from buying and selling stocks given a list of daily stock prices `prices` and a transaction fee `fee`. The function should consider that the stock must be bought before it can be sold and that a transaction fee is paid after each selling transaction.
"""

def maxProfit(prices, fee):
    n = len(prices)
    buy, sell = [0]*n, [0]*n
    buy[0] = -prices[0]  
    for i in range(1, n):
        buy[i] = max(buy[i-1], sell[i-1]-prices[i])  
        sell[i] = max(sell[i-1], buy[i-1]+prices[i]-fee)  
    return sell[n-1] 