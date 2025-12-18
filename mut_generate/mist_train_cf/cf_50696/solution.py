"""
QUESTION:
Write a function `minCost` that calculates the minimum cost of painting n houses with k colors, where no two adjacent houses have the same color, and the cost of painting each house with each color is given in the input `costs`. The input `costs` is a 2D array where `costs[i][j]` represents the cost of painting the `i-th` house with the `j-th` color. The function should return the minimum cost of painting all houses.
"""

def minCost(costs):
    if not costs: 
        return 0
    n, k = len(costs), len(costs[0])
    dp = [[float('inf')] * k for _ in range(n)]

    for j in range(k):
        dp[0][j] = costs[0][j]

    for l in range(1, n):    
        min1 = min2 = float('inf')
        idx1 = idx2 = -1
        for i in range(k):
            if dp[l-1][i] < min1:
                min2 = min1
                min1 = dp[l-1][i]
                idx2 = idx1
                idx1 = i
            elif dp[l-1][i] < min2:
                min2 = dp[l-1][i]
                idx2 = i
        for i in range(k):
            if i == idx1:
                if idx2 >= 0:
                    dp[l][i] = min(dp[l][i], costs[l][i] + dp[l-1][idx2])
            else:
                dp[l][i] = min(dp[l][i], dp[l-1][i] + costs[l][i])
        
    return min(dp[n-1])