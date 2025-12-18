"""
QUESTION:
Design a function `min_edit_distance(s1, s2)` that takes two strings `s1` and `s2` as inputs and returns the minimum number of operations (insertions, deletions, or substitutions) required to transform `s1` into `s2`.
"""

def min_edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j 
            elif j == 0:
                dp[i][j] = i 
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] 
            else:
                dp[i][j] = 1 + min(dp[i][j-1], 
                                   dp[i-1][j],  
                                   dp[i-1][j-1]  
                                  )
    return dp[m][n]