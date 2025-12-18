"""
QUESTION:
Write a function named `knapsack` that takes two lists, `weights` and `values`, and an integer `capacity`, as input. The function should return the maximum total value that can be put in a knapsack of the given capacity and the corresponding weights of the items included in the knapsack. The function should use dynamic programming to solve the 0/1 knapsack problem, where each item can either be included or excluded from the knapsack.
"""

def knapsack(weights, values, capacity):
    """
    This function solves the 0/1 knapsack problem using dynamic programming.
    
    Parameters:
    weights (list): A list of integers representing the weights of the items.
    values (list): A list of integers representing the values of the items.
    capacity (int): The maximum capacity of the knapsack.
    
    Returns:
    int: The maximum total value that can be put in a knapsack of the given capacity.
    list: The corresponding weights of the items included in the knapsack.
    """
    
    # Initialize a table to store the maximum value for each subproblem
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(values) + 1)]
    
    # Fill the table using dynamic programming
    for i in range(1, len(values) + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Reconstruct the solution by tracing back the table
    result = []
    i, j = len(values), capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            result.append(weights[i - 1])
            j -= weights[i - 1]
        i -= 1
    
    return dp[-1][-1], result