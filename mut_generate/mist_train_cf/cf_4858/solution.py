"""
QUESTION:
Write a function `minEditDistance(string1, string2)` that calculates the minimum number of operations (insertions, deletions, or substitutions) required to transform `string1` into `string2`. The function should take two parameters: `string1` and `string2`, which are the input strings. The function should return the minimum edit distance between the two strings.
"""

def minEditDistance(string1, string2):
    m = len(string1)
    n = len(string2)
    
    dp = [[0 for j in range(n+1)] for i in range(m+1)]
    
    for i in range(m+1):
        dp[i][0] = i
    
    for j in range(n+1):
        dp[0][j] = j
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
    
    return dp[m][n]