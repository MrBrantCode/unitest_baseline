"""
QUESTION:
Implement a function `longest_common_subsequence(str1, str2)` that takes two strings `str1` and `str2` as input, each with a minimum length of 15 characters. The function should return a tuple containing the longest common subsequence of uppercase alphabetical characters and its length. If there are multiple subsequences with the same length, return the one that comes first lexicographically.
"""

def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dynamic programming table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1] and str1[i - 1].isupper():
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Retrieve the longest common subsequence
    lcs_length = dp[m][n]
    lcs = [''] * lcs_length
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1] and str1[i - 1].isupper():
            lcs[lcs_length - 1] = str1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(lcs), len(lcs)