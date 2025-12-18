"""
QUESTION:
Write a function `knapsack(n, W, value, weight)` that uses the Bottom-Up Dynamic Programming approach to solve the 0/1 Knapsack problem. The function should take the following parameters:
- `n`: The number of items available.
- `W`: The weight capacity of the knapsack.
- `value`: An array containing the values of the items.
- `weight`: An array containing the weights of the items.
The function should return the maximum value achievable without exceeding the weight capacity.
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