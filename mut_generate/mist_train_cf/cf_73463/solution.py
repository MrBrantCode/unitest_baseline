"""
QUESTION:
The function `winnerSquareGame(n)` determines whether Alice can win the Stone Game IV given a positive integer `n` representing the number of stones. The game rules dictate that players can remove a non-zero square number of stones from the heap on their turn, and a player who cannot make a move loses. The function should return `True` if Alice can win and `False` otherwise. The input `n` is a positive integer where `1 <= n <= 10^5`.
"""

def winnerSquareGame(n: int) -> bool:
    dp = [False]*(n+1)
    for i in range(1,n+1):
        j = 1
        while j*j <= i and not dp[i]:
            dp[i] = dp[i] or not dp[i-j*j]
            j += 1
    return dp[-1]