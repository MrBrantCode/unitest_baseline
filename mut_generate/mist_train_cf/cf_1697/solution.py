"""
QUESTION:
Write a function `longest_common_subsequence(str1, str2)` that takes two strings as input and returns a tuple containing the length of the longest common subsequence and the actual subsequence itself. The function should have a time complexity of O(n*m), where n and m are the lengths of the input strings, respectively.
"""

def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    length = dp[m][n]

    subsequence = ''
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            subsequence = str1[i-1] + subsequence
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return length, subsequence