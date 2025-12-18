"""
QUESTION:
Implement a function N(a, b, c) that calculates the last 8 digits of the total number of configurations of type (a, b, c), where a and b represent the number of units A and B, and c is the maximum number of distinct colors used to color the graph vertices. The function should use modular arithmetic to efficiently compute the result modulo 10^8.
"""

def N(a, b, c):
    mod = 10**8
    dp = [[[0 for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)]
    dp[0][0][0] = 1
    for i in range(a+1):
        for j in range(b+1):
            for k in range(1, c+1):
                if i > 0:
                    dp[i][j][k] += dp[i-1][j][k-1]*k + dp[i-1][j][k]*2*i
                if j > 0:
                    dp[i][j][k] += dp[i][j-1][k-1]*k + dp[i][j-1][k]*2*j
                dp[i][j][k] %= mod
    return dp[-1][-1][-1]