"""
QUESTION:
Write a function `solve_trapezoid(trapezoid)` that takes a trapezoid-shaped grid of numbers as input and returns a single numerical value. The trapezoid-shaped grid is represented as a list of lists, where each inner list represents a row in the trapezoid. The function should calculate the maximum sum of the path from the top to the bottom, where each step can only move down to the directly below point or the point below and to the right. The input trapezoid-shaped grid will always be a valid trapezoid with at least one row.
"""

def entrance(trapezoid):
    dp = trapezoid[-1]
    for row in range(len(trapezoid)-2, -1, -1):
        for col in range(len(trapezoid[row])):
            dp[col] = max(dp[col], dp[col+1]) + trapezoid[row][col]
    return dp[0]