"""
QUESTION:
Write a function `longest_common_substring(s1, s2)` that takes two strings `s1` and `s2` as input and returns the longest common substring between them. The substring should contain only alphabetic characters. The function should have a time complexity of O(n^2), where n is the length of the longest string.
"""

def longest_common_substring(s1, s2):
    len1, len2 = len(s1), len(s2)
    dp = [[0] * (len2+1) for _ in range(len1+1)]
    maxLen = 0
    endIdx = 0

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if s1[i-1].isalpha() and s2[j-1].isalpha() and s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > maxLen:
                    maxLen = dp[i][j]
                    endIdx = i

    return s1[endIdx-maxLen:endIdx]