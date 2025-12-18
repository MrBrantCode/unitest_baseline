"""
QUESTION:
Write a function `knapsack_max_value(weights, values, capacity)` that calculates the maximum value that can be obtained by selecting a subset of the items such that the total weight does not exceed the given capacity. The function takes in three parameters: `weights`, a list of integers representing the weights of the items; `values`, a list of integers representing the values of the items; and `capacity`, an integer representing the maximum weight capacity of the knapsack. The function should return the maximum value that can be obtained by selecting a subset of the items.
"""

def knapsack_max_value(weights, values, capacity):
    n = len(weights)
    cell = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                cell[i][j] = max(cell[i-1][j], values[i - 1] + cell[i - 1][j - weights[i - 1]])
            else:
                cell[i][j] = cell[i - 1][j]

    return cell[n][capacity]