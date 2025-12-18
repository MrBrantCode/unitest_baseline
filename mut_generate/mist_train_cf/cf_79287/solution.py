"""
QUESTION:
Write a function `maxProfit(prices, fee)` that takes an array `prices` of stock prices and a fixed transaction fee `fee` as input, and returns the maximum profit that can be achieved by buying and selling stocks multiple times, where each transaction incurs the given fee. The function must follow these rules: 
- The function can complete as many transactions as desired, but it must pay the transaction fee for each transaction.
- The function cannot engage in multiple transactions simultaneously (i.e., it must sell the stock before buying again).
- The length of the `prices` array is between 1 and 3*10^4, inclusive.
- Each element in the `prices` array is between 0 and 10^4, inclusive.
- The transaction fee `fee` is between 0 and 10^4, inclusive.
"""

def maxProfit(prices, fee):
    n = len(prices)
    buy = [-prices[0]]
    sell = [0]

    for i in range(1, n):
        buy.append(max(buy[i - 1], sell[i - 1] - prices[i]))
        sell.append(max(sell[i - 1], buy[i - 1] + prices[i] - fee))

    return sell[-1]