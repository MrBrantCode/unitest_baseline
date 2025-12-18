"""
QUESTION:
Write a function `knapsack` that takes a list of items, where each item is a tuple of value and weight, and the capacity of a knapsack as input. The function should return the maximum total value that can be put in the knapsack without exceeding the capacity.

The function should take two parameters: `items`, a list of tuples where each tuple contains the value and weight of an item, and `capacity`, an integer representing the maximum weight capacity of the knapsack.
"""

def knapsack(items, capacity):
    n = len(items)

    # create a 2D array to save the maximum value
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # start from the first item
    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for j in range(1, capacity + 1):
            if j >= weight:
                # choose the larger one between packing and not packing the item
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity]