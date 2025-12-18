"""
QUESTION:
Write a function `longest_common_subsequence(str1, str2)` that takes two strings as input and returns their longest common subsequence. The function should have a time complexity of O(n*m), where n is the length of the first string and m is the length of the second string.
"""

def longest_common_subsequence(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lcs_length = dp[n][m]
    lcs = ""

    i = n
    j = m
    while i > 0 and j > 0:
        if str1[i-1] != str2[j-1]:
            if dp[i-1][j] >= dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        else:
            lcs = str1[i-1] + lcs
            i -= 1
            j -= 1

    return lcs