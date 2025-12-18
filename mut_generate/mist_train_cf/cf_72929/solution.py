"""
QUESTION:
Write a function `minFallingPathSumWithNonZeroShifts` that takes a 2D list of integers `arr` as input, where all elements are prime numbers, and returns the minimum sum of a falling path with non-zero shifts that only includes prime numbers. A falling path with non-zero shifts is a choice of exactly one element from each row of `arr`, such that no two elements chosen in adjacent rows are in the same column. The function should work under the constraints: `1 <= arr.length == arr[i].length <= 200` and `-99 <= arr[i][j] <= 99`.
"""

from typing import List

def minFallingPathSumWithNonZeroShifts(arr: List[List[int]]) -> int:
    n = len(arr)
    INF = float('inf')
    dp = [[INF] * (n+2) for _ in range(n+2)]
    for i in range(1, n+1):
        dp[n][i] = arr[n-1][i-1]
    for i in range(n-1, 0, -1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i+1][j-1], dp[i+1][j+1]) + arr[i-1][j-1]
    return min(dp[1])