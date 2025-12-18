"""
QUESTION:
Given the number of items (n), the weight capacity of the knapsack (W), and two arrays representing the values and weights of the items (value and weight), implement the function `knapsack(n, W, value, weight)` to determine the maximum value that can be obtained without exceeding the weight capacity of the knapsack using the Bottom-Up Dynamic Programming approach. The function should take four inputs: n (int), W (int), value (list of ints), and weight (list of ints), and return the maximum achievable value (int).
"""

def knapsack(n, W, value, weight):
    dp = [[0] * (W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if weight[i-1] <= w:
                dp[i][w] = max(value[i-1] + dp[i-1][w - weight[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][W]