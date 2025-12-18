"""
QUESTION:
Implement a function named `knapsack` that takes two lists, `weights` and `values`, representing the weights and values of items, respectively, and an integer `capacity` representing the maximum capacity of the knapsack. The function should return the maximum total value that can be put into the knapsack without exceeding the capacity, considering that each item can either be taken (1) or not (0), and it is not possible to take only a part of any item. The function should use the Dynamic Programming paradigm to solve the problem.
"""

def knapsack(weights, values, capacity):
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