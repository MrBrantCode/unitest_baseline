"""
QUESTION:
Count the number of strings of length `n` that consist only of vowels (`a`, `e`, `i`, `o`, `u`), are lexicographically sorted, and contain exactly `k` distinct vowels.

Function name: `countVowelStrings(n: int, k: int) -> int`

Restrictions:
- `1 <= n <= 50`
- `1 <= k <= 5`
"""

def countVowelStrings(n: int, k: int) -> int:
    dp = [[0] * (k+1) for _ in range(n+1)]
    for j in range(1, k+1):
        dp[0][j] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[n][k]