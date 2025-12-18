"""
QUESTION:
Function: knightDialer
Information: Given an integer `n`, determine the number of distinct phone numbers of length `n` that can be dialled by a chess knight on a phone pad, without any repeated consecutive digits. The knight can move two squares vertically and one square horizontally, or two squares horizontally and one square vertically, forming an L shape. The result should be returned modulo `10^9 + 7`.
Restrictions: `1 <= n <= 5000`.
"""

def knightDialer(n):
    mod = 10**9 + 7
    moves = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
    dp = [[0]*10 for _ in range(n)]
    for i in range(10):
        dp[0][i] = 1
    for i in range(1,n):
        for j in range(10):
            for k in moves[j]:
                dp[i][j] += dp[i-1][k]
                dp[i][j] %= mod
    return sum(dp[-1]) % mod