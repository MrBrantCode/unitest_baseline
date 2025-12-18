"""
QUESTION:
Write a function `count_valid_permutations` to calculate the number of valid permutations of length `2n` using `n` prime numbers and `n` non-prime numbers, where no two prime numbers can be adjacent in any valid permutation, and the prime numbers and non-prime numbers are distinct. The function should take an integer `n` as input and return the count of valid permutations modulo `10^9 + 7`.
"""

def count_valid_permutations(n):
    MOD = 10**9 + 7

    # dynamic programming table
    dp = [[0 for _ in range(n+1)] for __ in range(2*n+1)]

    # initialize base cases
    dp[0][0] = 1

    for i in range(1, 2*n+1):
        for j in range(min(i, n)+1):
            if j:
                # choose a prime
                dp[i][j] = dp[i-1][j-1] * (n-j+1)
                dp[i][j] %= MOD
            if j < i:
                # choose a non-prime
                dp[i][j] += dp[i-1][j] * (n-j)
                dp[i][j] %= MOD

    # valid permutations is sum of dp[2*n][j] over all even j
    ans = sum(dp[2*n][j] for j in range(0, n+1, 2))
    ans %= MOD
    return ans