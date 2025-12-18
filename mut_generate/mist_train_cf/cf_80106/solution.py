"""
QUESTION:
Define a function g(n) that calculates the count of unique colorings in an n x n square grid, where each cell can be either black or white, and each row and column must contain exactly two black cells, considering rotations and reflections. The function should return the result modulo 1,000,000,007.
"""

def g(n):
    MOD = 1000000007

    def f(n):  
        dp = [1] + [0] * n
        for _ in range(n):
            new_dp = dp[:]
            for i in range(n, 1, -1):
                new_dp[i] = (new_dp[i] * i + 2 * new_dp[i-1] * (n-i+2)) % MOD
            new_dp[1] = new_dp[1] * 2 % MOD
            dp = new_dp    
        return dp[n]

    return f(n) * pow(8, MOD-2, MOD) % MOD