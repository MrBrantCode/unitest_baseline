"""
QUESTION:
Given a matrix representing the cost of traveling from one city to another with dimensions `n x 3`, where `n` is the number of cities and each row represents a city with three columns for the cost of traveling to the next city in three different modes of transportation, write a function `minCostTravel(matrix)` to calculate the minimum cost of travel from the first city to the last city, with the constraint that you cannot use the same mode of transportation in two consecutive cities. The function should take a 2D list of integers as input and return an integer representing the minimum cost of travel.
"""

from typing import List

def minCostTravel(matrix: List[List[int]]) -> int:
    n = len(matrix)
    if n == 1:
        return min(matrix[0])

    dp = [[0, 0, 0] for _ in range(n)]
    dp[0] = matrix[0]

    for i in range(1, n):
        dp[i][0] = matrix[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = matrix[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = matrix[i][2] + min(dp[i-1][0], dp[i-1][1])

    return min(dp[n-1])