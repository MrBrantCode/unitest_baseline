"""
QUESTION:
Write a function `isInterleave(s1, s2, s3)` that determines if `s3` is an interleaving of `s1` and `s2`. The function should return a boolean value. The lengths of `s1`, `s2`, and `s3` are less than or equal to 100. The function does not need to handle any exceptions.
"""

def isInterleave(s1, s2, s3):
    len1, len2, len3 = len(s1), len(s2), len(s3)
    if len1 + len2 != len3:
        return False

    dp = [[False]*(len2+1) for _ in range(len1+1)]

    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
            else:
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

    return dp[len1][len2]