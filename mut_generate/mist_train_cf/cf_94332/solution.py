"""
QUESTION:
Write a function `longest_common_subsequence(str1, str2)` that finds the longest common subsequence of two given strings and returns its length and the actual subsequence. The function should have a time complexity of O(n*m), where n and m are the lengths of the input strings, respectively. The function should handle cases where the input strings contain special characters, spaces, and uppercase/lowercase letters.
"""

def longest_common_subsequence(str1, str2):
    n, m = len(str1), len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    length = dp[n][m]
    subsequence = ""
    i, j = n, m

    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            subsequence += str1[i-1]
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    subsequence = subsequence[::-1]

    return length, subsequence