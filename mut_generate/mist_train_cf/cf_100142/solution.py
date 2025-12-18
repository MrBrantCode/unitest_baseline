"""
QUESTION:
Write a function `stoneGame` that takes a list of positive integers `piles` as input, representing the number of stones in each pile arranged in a row, and returns a boolean value indicating whether Alex wins or loses the game. The game is played by two players, Alex and Lee, who take turns picking the entire pile of stones from either the beginning or the end of the row, with the objective of ending with the most stones. The total number of stones is odd, and Alex starts first.
"""

from typing import List

def stoneGame(piles: List[int]) -> bool:
    n = len(piles)
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = piles[i]
    for d in range(1, n):
        for i in range(n-d):
            j = i+d
            dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
    return dp[0][-1] > 0