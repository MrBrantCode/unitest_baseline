"""
QUESTION:
Write a function `knapsack_max_value` that takes three parameters: a list of item weights, a list of corresponding item values, and the knapsack capacity. The function should return the maximum value that can be obtained by selecting a subset of the items to fit into the knapsack without exceeding its capacity. The function should assume that the input lists are of the same length and that the weights and capacity are non-negative integers, and the values are non-negative numbers.
"""

def knapsack_max_value(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]