"""
QUESTION:
You are given a function `numWays` that takes two integers `steps` and `arrLen` as input. The function should return the number of ways to move a pointer in an array of size `arrLen` such that it is at index `1` after exactly `steps` steps. The pointer can move 1 position to the left, 1 position to the right, or stay in the same place at each step, and it should not be placed outside the array at any time. The result should be returned modulo `10^9 + 7`.

Restrictions:
- `1 <= steps <= 500`
- `1 <= arrLen <= 10^6`
"""

def numWays(steps, arrLen):
    MOD = 10**9 + 7
    dp = [[0 for _ in range(min(arrLen, steps + 1))] for _ in range(steps + 1)]
    
    dp[0][0] = 1
    
    for i in range(steps):
        for j in range(min(i+2, arrLen)):
            dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD
            if j > 0:
                dp[i+1][j] = (dp[i+1][j] + dp[i][j-1]) % MOD
            if j < min(i+2, arrLen) - 1:
                dp[i+1][j] = (dp[i+1][j] + dp[i][j+1]) % MOD
                
    return dp[steps][1]