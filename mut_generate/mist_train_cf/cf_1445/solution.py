"""
QUESTION:
Write a function `longest_common_substring(s, t)` that takes two input strings `s` and `t` and returns the length of the longest common substring that starts and ends with the same character and has at least one vowel. A vowel is defined as 'a', 'e', 'i', 'o', or 'u'.
"""

def longest_common_substring(s, t):
    m = len(s)
    n = len(t)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1] and s[i - 1] in ['a', 'e', 'i', 'o', 'u']:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len and i - dp[i][j] == j - dp[i][j]:
                    max_len = dp[i][j]
            else:
                dp[i][j] = 0
    
    return max_len