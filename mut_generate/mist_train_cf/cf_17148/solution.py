"""
QUESTION:
Write a function called `knapsack` that takes in a list of items, where each item is a list containing its value and weight, and a knapsack capacity, and returns the maximum value that can be achieved with the given items and capacity, considering that the items must be selected in the order they appear in the list. The function should also return the actual items selected to achieve this maximum value.
"""

def knapsack(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            value, weight = items[i - 1]
            if weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], value + dp[i - 1][j - weight])

    max_value = dp[n][capacity]
    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        value, weight = items[i - 1]
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append((value, weight))
            j -= weight
        i -= 1

    return max_value, selected_items[::-1]