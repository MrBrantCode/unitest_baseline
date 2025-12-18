"""
QUESTION:
Given a triangle represented as a list of lists where each list represents a row of the triangle, find the minimum path sum from the top to the bottom of the triangle. Each step can move to the adjacent numbers on the row below. Write a function `minimumTotal(triangle)` that takes in the triangle and returns the minimum path sum.
"""

from typing import List

def minimumTotal(triangle: List[List[int]]) -> int:
    size = len(triangle)
    dp = [0] * size
    for i in range(size):
        dp[i] = triangle[size - 1][i]
    for i in range(size - 2, -1, -1):
        for j in range(i + 1):
            dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
    return dp[0]