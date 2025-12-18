"""
QUESTION:
Implement a function called `levenshtein_distance` to calculate the Levenshtein distance between two strings, which is a measure of the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other. The function should take two parameters, `str1` and `str2`, both of which are strings, and return an integer representing the Levenshtein distance.
"""

def levenshtein_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    
    return dp[m][n]