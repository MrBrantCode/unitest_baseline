"""
QUESTION:
Write a function named `knapsack` that takes in a list of items where each item is a tuple of its weight and value, and an integer `W` representing the weight limit of the knapsack. The function should return the maximum total value that can be achieved without exceeding the weight limit. The items are either taken once or not at all (i.e., 0 or 1 times).
"""

def knapsack(items, W):
    n = len(items)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for w in range(1, W + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]