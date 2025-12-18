"""
QUESTION:
Write a function called `levenshtein_distance` that takes as input two strings `str1` and `str2`, and an integer `limit` that specifies the maximum allowed length of the final string. The function should return the minimum number of edits (insertions, deletions, or substitutions) required to transform `str1` into `str2` and the sequence of edits required. If the length of the final string exceeds the specified limit, the function should handle it accordingly.
"""

def levenshtein_distance(str1, str2, limit):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    edits = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
            i -= 1
            j -= 1
        elif j > 0 and (i == 0 or dp[i][j] == dp[i][j - 1] + 1):
            edits.append(f"Insert '{str2[j - 1]}'")
            j -= 1
        elif i > 0 and (j == 0 or dp[i][j] == dp[i - 1][j] + 1):
            edits.append(f"Delete '{str1[i - 1]}'")
            i -= 1
        else:
            edits.append(f"Substitute '{str1[i - 1]}' with '{str2[j - 1]}'")
            i -= 1
            j -= 1

    if len(str2) > limit:
        return dp[m][n], edits, str2[:limit]
    else:
        return dp[m][n], edits, str2