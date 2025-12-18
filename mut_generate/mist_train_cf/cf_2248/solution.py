"""
QUESTION:
Implement a function named `knapsack` that takes in four parameters: `values`, `weights`, `capacity`, and `n`. The function should return the maximum value that can be obtained by selecting a subset of items from the given list of values and weights, without exceeding the given capacity. The items must be selected in a specific order based on their values and weights, and the function should minimize the total weight of the selected items while maximizing their total value. The time complexity of the solution should be O(n*W).
"""

def knapsack(values, weights, capacity, n):
    """
    Returns the maximum value that can be obtained by selecting a subset of items 
    from the given list of values and weights, without exceeding the given capacity.

    Parameters:
    values (list): List of item values
    weights (list): List of item weights
    capacity (int): Maximum weight capacity
    n (int): Number of items

    Returns:
    int: Maximum value that can be obtained
    """
    # Create a 2D table to store the maximum value at each subproblem
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Iterate through each item
    for i in range(1, n + 1):
        # Iterate through each possible weight from 0 to capacity
        for w in range(1, capacity + 1):
            # If the weight of the current item is less than or equal to the current weight
            if weights[i - 1] <= w:
                # Choose the maximum value between including and not including the item
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # The weight of the current item is greater than the current weight
                # Copy the value from the previous row
                dp[i][w] = dp[i - 1][w]

    # Return the maximum value that can be obtained with the given capacity constraint
    return dp[n][capacity]