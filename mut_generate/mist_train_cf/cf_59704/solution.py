"""
QUESTION:
Write a function `lcs(str1, str2)` that takes two distinct input strings `str1` and `str2` and returns the longest common subsequence found within them. The function should find the subsequence that appears in the same relative order in both strings, but it may not be contiguous.
"""

def findLCS(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

    index = dp[m][n]
    lcs_ = [""] * (index+1)
    lcs_[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs_[index-1] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i-=1
        else:
            j-=1

    result = "".join(lcs_)
    return result