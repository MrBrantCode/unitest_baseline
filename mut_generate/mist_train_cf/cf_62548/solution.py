"""
QUESTION:
You are given an integer array `values` representing the values of the vertices of a convex polygon, where `values[i]` corresponds to the value of the `ith` vertex, arranged in a clockwise sequence. Your task is to determine the least possible total score achievable through any possible triangulation of the polygon, where each triangle's value is the product of its vertices' values and the total score of the triangulation is the cumulative sum of these values across all triangles.

Implement a function named `minScoreTriangulation` that takes `values` as input and returns the minimum total score. The function should satisfy the constraints that `3 <= n <= 50` and `1 <= values[i] <= 100`, where `n` is the length of `values`.
"""

def minScoreTriangulation(values):
    dp = [[0]*60 for _ in range(60)]
    n = len(values)
    for range_ in range(2, n):
        for left in range(0, n-range_):
            right = left + range_
            dp[left][right] = min(dp[left][k] + dp[k][right] + values[left]*values[right]*values[k] for k in range(left+1,right))
    return dp[0][n-1]