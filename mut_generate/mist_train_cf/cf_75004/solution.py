"""
QUESTION:
Implement a function `maxProfit(prices, fee)` that calculates the maximum possible profit from buying and selling stocks given a list of stock prices `prices` and a brokerage fee `fee`. The function should return the highest achievable profit. The function is allowed to perform unlimited transactions, but each transaction incurs the brokerage fee and concurrent transactions are not allowed. The input constraints are `1 <= len(prices) <= 5 * 10^4`, `1 <= prices[i] <= 5 * 10^4`, and `0 <= fee <= 5 * 10^4`.
"""

def maxProfit(prices, fee):
    buy, sell = -prices[0], 0
    for price in prices[1:]:
        buy, sell = max(buy, sell-price), max(sell, buy+price-fee)
    return sell