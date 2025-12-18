"""
QUESTION:
Write a function `knapsack(weights, values, capacity, valueLimit)` that takes in four parameters: 
- `weights`: An array of item weights.
- `values`: An array of item values.
- `capacity`: The maximum weight capacity of the knapsack.
- `valueLimit`: The maximum value limit of any item.

The function should return the maximum value that can be obtained from a 0/1 knapsack problem where each item can be taken at most once and the maximum value of any item does not exceed the given limit.
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