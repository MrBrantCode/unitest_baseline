"""
QUESTION:
Implement a function `levenshtein_distance(s1, s2)` that calculates the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string `s1` into another string `s2`. The function should take two strings `s1` and `s2` as input and return the minimum number of edits required to transform `s1` into `s2`.
"""

def levenshtein_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]