"""
QUESTION:
Implement a function `max_value_knapsack` that takes in four parameters: `weights`, `values`, `limits`, and `capacity`. The function should return the maximum value that can be obtained by selecting a combination of items such that the total weight does not exceed the capacity, and the number of times each item is selected does not exceed its limit. The parameters are defined as follows:
- `weights`: A list of integers representing the weights of the items.
- `values`: A list of integers representing the values of the items.
- `limits`: A list of integers representing the limits on the number of times each item can be included.
- `capacity`: An integer representing the maximum weight the knapsack can hold.
"""

def max_value_knapsack(weights, values, limits, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            for k in range(min(limits[i - 1], j // weights[i - 1]) + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k * weights[i - 1]] + k * values[i - 1])

    return dp[-1][-1]