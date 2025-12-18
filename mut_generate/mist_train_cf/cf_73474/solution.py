"""
QUESTION:
Write a function `countVowelPermutation(n)` that calculates the number of unique strings of length `n` constructed from lower case vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`) with the following rules:
- `'a'` can only be succeeded by `'e'`.
- `'e'` can only be succeeded by `'a'` or `'i'`.
- `'i'` cannot be succeeded by another `'i'`.
- `'o'` can only be succeeded by `'i'` or `'u'`.
- `'u'` can only be succeeded by `'a'`.
Return the count modulo `10^9 + 7`.

The function should take a positive integer `n` as input where `1 <= n <= 2 * 10^4`.
"""

def countVowelPermutation(n):
    dp = [[0]*n for _ in range(5)]
    MOD = 10**9 + 7

    for i in range(5):
        dp[i][0] = 1

    for j in range(1, n):
        dp[0][j] = dp[1][j - 1]
        dp[1][j] = (dp[0][j - 1] + dp[2][j - 1]) % MOD
        dp[2][j] = (dp[0][j - 1] + dp[1][j - 1] + dp[3][j - 1] + dp[4][j - 1]) % MOD
        dp[3][j] = (dp[2][j - 1] + dp[4][j - 1]) % MOD
        dp[4][j] = dp[0][j - 1]
        
    return sum(dp[i][n - 1] for i in range(5)) % MOD