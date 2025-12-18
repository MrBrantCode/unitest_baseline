"""
QUESTION:
You are given an array `piles` where `piles[i]` represents the number of stones in the `i`-th pile. Write a function `stoneGame(piles)` that determines whether the first player can win the game by taking turns to pick either the first or last pile from the array, assuming both players play optimally. The function should return `True` if the first player can win, and `False` otherwise.
"""

def stoneGame(piles):
    n = len(piles)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = piles[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])

    return dp[0][n - 1] > 0