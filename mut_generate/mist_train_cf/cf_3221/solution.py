"""
QUESTION:
Write a function called `knapsack` that takes four inputs: `weights`, an array of item weights; `values`, an array of item values; `capacity`, the maximum weight capacity of the knapsack; and `valueLimit`, the maximum value limit of any item. Implement a dynamic programming algorithm to solve the 0/1 knapsack problem with the additional constraint that each item can be taken at most once, the maximum weight capacity of the knapsack should not be exceeded, and the maximum value of any item should not exceed the given limit.
"""

def knapsack(weights, values, capacity, valueLimit):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for weight in range(1, capacity + 1):
            if weights[i - 1] > weight:
                dp[i][weight] = dp[i - 1][weight]
            else:
                if values[i - 1] <= valueLimit:
                    dp[i][weight] = max(dp[i - 1][weight], dp[i - 1][weight - weights[i - 1]] + values[i - 1])
                else:
                    dp[i][weight] = dp[i - 1][weight]

    return dp[n][capacity]