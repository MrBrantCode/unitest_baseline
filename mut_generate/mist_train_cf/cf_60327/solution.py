"""
QUESTION:
Write a function named `knapsack` that takes in a list of item weights, a list of corresponding item values, and a knapsack weight limit, and returns the maximum value that can be achieved without exceeding the knapsack weight limit. The function should consider that each item can either be included or excluded, and the goal is to maximize the total value while not surpassing the weight limit.
"""

def knapsack(weights, values, capacity):
    """
    Returns the maximum value that can be achieved without exceeding the knapsack weight limit.
    
    Parameters:
    weights (list): A list of item weights.
    values (list): A list of corresponding item values.
    capacity (int): The knapsack weight limit.
    
    Returns:
    int: The maximum value that can be achieved.
    """
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]],  dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]