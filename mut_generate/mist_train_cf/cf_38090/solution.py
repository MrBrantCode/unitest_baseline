"""
QUESTION:
Write a function `minEditDistance` that takes two strings `source` and `target` as input and returns the minimum number of operations (insertions, deletions, or replacements) required to transform `source` into `target`. The transformation is case-insensitive.
"""

def minEditDistance(source: str, target: str) -> int:
    m, n = len(source), len(target)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif source[i - 1].lower() == target[j - 1].lower():
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

    return dp[m][n]