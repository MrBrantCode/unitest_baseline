"""
QUESTION:
Create a function `knapsack_dp` that implements the dynamic programming approach to solve the 0/1 knapsack problem. The function takes three parameters: `weights`, `values`, and `capacity`, where `weights` and `values` are lists of integers representing the weights and values of items respectively, and `capacity` is an integer representing the maximum weight the knapsack can hold. The function should return the maximum value that can be put in a knapsack of the given capacity.
"""

def knapsack_dp(weights, values, capacity):
    """
    This function implements the dynamic programming approach to solve the 0/1 knapsack problem.
    
    Parameters:
    weights (list): A list of integers representing the weights of items.
    values (list): A list of integers representing the values of items.
    capacity (int): An integer representing the maximum weight the knapsack can hold.
    
    Returns:
    int: The maximum value that can be put in a knapsack of the given capacity.
    """
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