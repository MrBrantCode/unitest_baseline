"""
QUESTION:
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day and an integer `k` representing the cooldown period after selling a stock. 

Implement a function `maxProfit(prices, k)` to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock, with the restriction that you cannot buy another stock for `k` days after selling. If no profit can be achieved, return `0`. 

Constraints: `1 <= prices.length <= 10^5`, `0 <= prices[i] <= 10^4`, and `1 <= k <= prices.length`.
"""

def entance(prices, k):
    if not prices or k >= len(prices):
        return 0

    n = len(prices)

    buy = [-prices[0]] * n
    sell = [0] * n
    cooldown = [0] * n

    for i in range(1, n):
        cooldown[i] = max(cooldown[i-1], sell[i-1])

        if i > k:
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            buy[i] = max(buy[i-1], cooldown[i-k-1] - prices[i])
        else:
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            buy[i] = max(buy[i-1], -prices[i])

    return max(sell[-1], cooldown[-1])