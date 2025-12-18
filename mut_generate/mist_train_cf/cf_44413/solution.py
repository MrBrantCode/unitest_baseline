"""
QUESTION:
Write a function `S(n)` that calculates the sum of the total number of distinct methods to remove all bottles from a stack with `k` tiers, for `k` ranging from 1 to `n`, modulo 1,000,000,033. The function should take an integer `n` as input and return the result of the calculation. The function should use memoization and dynamic programming to solve the problem efficiently. The result should be returned modulo 1,000,000,033.
"""

MOD = 10**9+33

def S(n):
    dp = [[[0]*3 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(1,n+1):
        dp[i][i][0] = dp[i][i][1] = dp[i][i][2] = dp[i-1][i-1][0]
        for j in range(i-1,-1,-1):
            dp[i][j][0] = (dp[i-1][j][0]+dp[i-1][j][1]+dp[i-1][j][2])%MOD
            dp[i][j][1] = (dp[i][j+1][0]+dp[i][j+1][1])%MOD
            dp[i][j][2] = dp[i][j+1][2]
            if j<i-1: dp[i][j][2] = (dp[i][j][2]+dp[i][j+2][2])%MOD
    s = summ = 0
    for i in range(1,n+1):
        s = (s+dp[i][0][0])%MOD
        summ = (summ+s)%MOD
    return summ