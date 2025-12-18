"""
QUESTION:
Create a function `knapsack` that takes four parameters: an array of item weights, an array of item values, the maximum weight capacity of the knapsack, and the number of items available. The function should return the maximum value that can be obtained from the knapsack and the items included to achieve this value, given that each item can either be included or excluded.
"""

def knapsack(weights, values, capacity, numItems):
    dp = [[0] * (capacity + 1) for _ in range(numItems + 1)]

    for i in range(1, numItems + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    maxValue = dp[numItems][capacity]

    totalValue = maxValue
    includedItems = []
    for i in range(numItems, 0, -1):
        if dp[i][capacity] != dp[i - 1][capacity]:
            includedItems.append(i)
            capacity -= weights[i - 1]

    return maxValue, includedItems