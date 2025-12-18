"""
QUESTION:
Write a function `longest_common_substring(s1, s2)` to return the longest common substring between two input strings `s1` and `s2`. The strings may contain uppercase and lowercase letters, numbers, and special characters, and the comparison should be case insensitive. The function should return the longest common substring in the original case as it appears in `s1`.
"""

def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1].lower() == s2[j - 1].lower():
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
            else:
                dp[i][j] = 0
    return s1[end_index - max_length + 1:end_index + 1]