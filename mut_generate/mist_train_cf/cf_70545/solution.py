"""
QUESTION:
Given a string `s` of digits and an integer `k`, write a function `numberOfArrays` that returns the number of possible arrays that can be printed as a string `s` with all integers in the range `[1, k]` and no leading zeros, and must be sorted in non-decreasing order. The number of ways could be very large so return it modulo `10^9 + 7`.
"""

def numberOfArrays(s, k):
    n = len(s)
    MOD = 10**9 + 7
    dp = [[0]*3 for _ in range(n+1)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(3):
            if s[i] == '0': 
                if j == 1: dp[i+1][1] = dp[i][j]
            elif int(s[i]) < k % 10:
                if j == 0: dp[i+1][0] = dp[i][j]
                elif j == 1: dp[i+1][1] = dp[i][j]
                elif j == 2: dp[i+1][2] = dp[i][j]
            elif int(s[i]) == k % 10:
                if j == 0: dp[i+1][0] = dp[i][j]
                elif j == 1: dp[i+1][1] = dp[i][j]
                elif j == 2: dp[i+1][2] = dp[i][j]
            else:
                if j == 2: dp[i+1][2] = dp[i][j]
        k //= 10
        
    return (dp[n][0] + dp[n][1] + dp[n][2]) % MOD