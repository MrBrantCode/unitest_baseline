"""
QUESTION:
Create a function `knapsack` that takes two lists of integers `weights` and `values` representing the weights and values of items, an integer `numberOfItems` representing the number of items, and an integer `capacity` representing the maximum weight capacity. The function should return the maximum value that can be obtained without exceeding the given capacity.
"""

def knapsack(weights, values, numberOfItems, capacity):
    # Create DP table
    dp = [[0 for w in range(capacity + 1)] for i in range(numberOfItems + 1)]
    
    # Build table in bottom up manner
    for i in range(numberOfItems + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
 
    return dp[numberOfItems][capacity]