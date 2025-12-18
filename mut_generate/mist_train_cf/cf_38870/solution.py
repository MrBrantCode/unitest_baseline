"""
QUESTION:
Write a function `isKPal` that takes in three parameters: `str1` and `str2` (strings) and `k` (integer). The function should return `True` if it is possible to convert `str1` into `str2` using at most `k` operations (insertions, deletions, or replacements), and `False` otherwise.
"""

def isKPal(str1, str2, k):
    m, n = len(str1), len(str2)
    if abs(m - n) > k:
        return False

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n] <= k