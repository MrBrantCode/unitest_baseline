"""
QUESTION:
Create a function called `calculate_levenshtein_distance` that takes two strings `str1` and `str2` as input and returns the minimum number of single-character edits (insertions, deletions, or substitutions) required to transform `str1` into `str2`.
"""

def calculate_levenshtein_distance(str1, str2):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    for i in range(len(str1) + 1):
        dp[i][0] = i
        
    for j in range(len(str2) + 1):
        dp[0][j] = j
        
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    
    return dp[len(str1)][len(str2)]