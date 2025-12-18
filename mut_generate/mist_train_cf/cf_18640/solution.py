"""
QUESTION:
Implement the function levenshtein_distance(s1, s2) to calculate the Levenshtein distance between two strings s1 and s2, ensuring the solution has a time complexity of O(m*n), where m and n are the lengths of the input strings. The Levenshtein distance is defined as the minimum number of operations (insertions, deletions, or substitutions) required to transform one string into the other.
"""

def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Calculate dp[i][j] for all positions
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

    return dp[m][n]