"""
QUESTION:
Given an integer n, return the number of distinct phone numbers of length n that can be dialed using a chess knight on a phone pad, where the knight can only stand on numeric cells (i.e., blue cells), the phone number should not contain any repeated consecutive digits, and must not start with 0. The answer should be returned modulo 10^9 + 7.

The chess knight's movements are as follows: it can move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of the chess knight are shown in the diagram. 

You are allowed to place the knight on any numeric cell initially (except 0) and then perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

Function name: knightDialer
Parameter: n, an integer representing the length of the phone number.
Restrictions: 1 <= n <= 5000
"""

MOD = 10**9 + 7
jumps = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]

def knightDialer(n):
    dp = [[0]*10 for _ in range(n+1)]
    for j in range(10):
        dp[1][j] = 1
    for i in range(2, n+1):
        for j in range(10):
            for k in jumps[j]:
                dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    return sum(dp[n][1:]) % MOD