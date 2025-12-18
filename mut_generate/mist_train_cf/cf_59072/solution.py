"""
QUESTION:
Implement a function `shortestCommonSupersequence(str1, str2)` that returns the shortest string that has both `str1` and `str2` as subsequences, given the constraints that the supersequence should not contain any repeating sequence of characters from `str1` or `str2` that is longer than 2 characters, and it should start with the first character of `str1` and end with the last character of `str2`. The input strings `str1` and `str2` consist of lowercase English letters and their lengths are between 1 and 1000.
"""

def shortestCommonSupersequence(str1, str2):
    m, n = len(str1), len(str2)

    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    supersequence = ''
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            supersequence = str1[i-1] + supersequence
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            supersequence = str1[i-1] + supersequence
            i -= 1
        else:
            supersequence = str2[j-1] + supersequence
            j -= 1
    supersequence = str1[:i] + str2[:j] + supersequence

    result = ''
    for ch in supersequence:
        if result[-2:] != ch * 2:
            result += ch

    return result