"""
QUESTION:
Create a function named `longest_common_substring` that takes two strings `s1` and `s2` as input and returns their longest common substring. The function should have a time complexity of O(n*m), where n and m are the lengths of `s1` and `s2` respectively.
"""

def longest_common_substring(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    max_len = 0
    end_index = 0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i - 1
    longest_substring = s1[end_index - max_len + 1: end_index + 1]
    return longest_substring