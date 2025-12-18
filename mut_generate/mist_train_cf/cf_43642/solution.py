"""
QUESTION:
Write a function called `maxProfit` that takes three parameters: `k`, `prices`, and `fee`. The function should return the maximum profit that can be achieved by completing at most `k` transactions, where `prices` is a list of stock prices and `fee` is the transaction fee. The function should consider that you need to pay a transaction fee for each transaction you make, and you may not engage in multiple transactions simultaneously. The constraints are `0 <= k <= 100`, `0 <= len(prices) <= 1000`, `0 <= prices[i] <= 1000`, and `0 <= fee <= 1000`.
"""

def maxProfit(k, prices, fee):
    if not prices:
        return 0

    dp = [[-float('inf')]*2 for _ in range(k+1)]
    dp[0][1] = 0
    for i in range(1, len(prices)):
        for j in range(k, 0, -1):
            dp[j][0] = max(dp[j][0], dp[j-1][1] - prices[i])
            dp[j][1] = max(dp[j][1], dp[j][0] + prices[i] - fee)
    return max(dp[j][1] for j in range(k+1))