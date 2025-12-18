"""
QUESTION:
Write a function `minEdits(s1, s2)` that calculates the minimum number of edits (insertions, deletions, and substitutions) required to convert string `s1` to string `s2`.
"""

def minEdits(s1, s2):
    len1 = len(s1)
    len2 = len(s2)

    dp = [[0 for x in range(len2+1)]for x in range(len1+1)]

    for i in range(len1+1):
        for j in range(len2+1):

            if i == 0:
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1 + min(dp[i][j-1], 
                                   dp[i-1][j], 
                                   dp[i-1][j-1]) 

    return dp[len1][len2]