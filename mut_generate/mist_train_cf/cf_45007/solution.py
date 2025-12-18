"""
QUESTION:
Write a function `minCost(houses, cost, m, n, target, discount)` that calculates the minimum cost to paint all houses with certain rules. 

The function takes six parameters: 
- `houses` is a list of integers representing the colors of houses, where `houses[i]` is the color of the ith house and 0 represents the house is not painted yet.
- `cost` is a 2D list where `cost[i][j]` is the cost to paint the ith house with color j+1.
- `m` is the number of houses.
- `n` is the number of colors.
- `target` is the target number of neighborhoods.
- `discount` is a list of integers representing the discount when painting a house with the same color as the previous house.

The function should return the minimum cost if it is possible to paint all houses into `target` neighborhoods, otherwise return -1.
"""

import sys

def minCost(houses, cost, m, n, target, discount):
    dp = [[[sys.maxsize]*n for _ in range(target+1)] for _ in range(m+1)]
    dp[0][0] = [0]*n

    for i in range(m):
       for j in range(i+1):
          for k in range(n):
              if j+i <= target:
                 if houses[i] == 0 or houses[i]-1 == k:
                     for l in range(n):
                        if l == k:
                            dp[i+1][j+1][k] = min(dp[i+1][j+1][k], dp[i][j][l]+cost[i][k])
                        else:
                            dp[i+1][j+1][k] = min(dp[i+1][j+1][k], dp[i][j][l]+cost[i][k]-discount[i])

                 if houses[i]-1 == k or houses[i] == 0:
                    dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k]+cost[i][k]-discount[i])

    return min(dp[m][target]) if min(dp[m][target]) != sys.maxsize else -1