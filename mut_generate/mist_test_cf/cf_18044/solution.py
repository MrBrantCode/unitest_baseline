"""
QUESTION:
Write a function called `knapsack` that solves the 0/1 knapsack problem using dynamic programming, where each item can be taken at most once. The function should take in the following parameters: the maximum capacity `W` of the knapsack, the `weights` of the items, and their corresponding `values`. The function should return the maximum value that can be obtained and the list of selected items. Assume that the number of items `n` is equal to the length of the `weights` or `values` arrays.
"""

def knapsack(W, weights, values):
    """
    Solves the 0/1 knapsack problem using dynamic programming.

    Args:
        W (int): The maximum capacity of the knapsack.
        weights (list): The weights of the items.
        values (list): The values of the items.

    Returns:
        tuple: A tuple containing the maximum value that can be obtained and the list of selected items.
    """
    n = len(weights)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])

    max_value = dp[n][W]
    selected_items = []
    j = W
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]

    return max_value, selected_items[::-1]