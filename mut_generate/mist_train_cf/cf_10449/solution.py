"""
QUESTION:
Write a function named `knapsack` that uses dynamic programming to solve the Knapsack problem. The function should take two parameters: a list of items, where each item is represented as a list of two integers, the first integer representing the weight of the item and the second integer representing the value of the item; and an integer representing the weight limit of the knapsack. The function should return the maximum value that can be achieved by selecting items without exceeding the weight limit. The function should have a time complexity of O(nW), where n is the number of items and W is the weight limit.
"""

def knapsack(items, weight_limit):
    """
    Solves the Knapsack problem using dynamic programming.

    Args:
    items (list): A list of items, where each item is represented as a list of two integers,
                  the first integer representing the weight of the item and the second integer
                  representing the value of the item.
    weight_limit (int): The weight limit of the knapsack.

    Returns:
    int: The maximum value that can be achieved by selecting items without exceeding the weight limit.
    """

    # Initialize a table to store the maximum value for each subproblem
    dp = [[0] * (weight_limit + 1) for _ in range(len(items) + 1)]

    # Iterate through each item and weight limit combination
    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]
        for w in range(1, weight_limit + 1):
            # If the weight of the current item exceeds the weight limit, exclude it
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            # Otherwise, choose the maximum value between including and excluding the current item
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    # The maximum value that can be achieved is stored in the last cell of the table
    return dp[-1][-1]