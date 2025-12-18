"""
QUESTION:
Write a function `winnerSquareGame(n)` that determines whether Alice can win a game with `n` stones. In this game, Alice and Bob take turns removing a non-zero square number of stones. If a player cannot make a move, they lose. Return `True` if Alice can win and `False` otherwise. Assume both players play optimally. `n` is a positive integer between 1 and 10^5.
"""

def winnerSquareGame(n: int) -> bool:
    dp = [False] * (n + 1)
    for i in range(1, n + 1):
        j = 1
        while j * j <= i and not dp[i]:
            dp[i] = not dp[i - j * j]
            j += 1
    return dp[n]