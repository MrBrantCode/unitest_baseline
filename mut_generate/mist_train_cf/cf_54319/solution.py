"""
QUESTION:
Write a function `maxProfit(prices, fee)` that takes an array `prices` of stock prices and a non-negative integer `fee` representing a transaction fee, and returns the maximum profit that can be achieved by buying and selling the stock with the following restrictions: 

- You must sell the stock before you buy again.
- You cannot buy stock on the next day after selling.
- You need to pay the transaction fee for every transaction.

The function should work with the constraint that `1 <= len(prices) <= 5000` and `0 <= prices[i], fee <= 1000`.
"""

def maxProfit(prices, fee):
    sold = [0] * len(prices)
    hold = [0] * len(prices)
    hold[0] = -prices[0]

    for i in range(1, len(prices)):
        sold[i] = max(sold[i-1], hold[i-1] + prices[i] - fee)
        hold[i] = max(hold[i-1], sold[i-2] - prices[i] if (i>=2) else -prices[i])

    return max(sold[-1], hold[-1])