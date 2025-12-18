"""
QUESTION:
Write a function `longest_common_substring(str1, str2)` that finds and returns the longest common substring between two input strings `str1` and `str2`. The function should return the longest contiguous substring that appears in both `str1` and `str2`.
"""

def longest_common_substring(str1, str2):
    n, m = len(str1), len(str2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    max_length = 0
    end_pos = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_pos = i
    return str1[end_pos-max_length : end_pos]