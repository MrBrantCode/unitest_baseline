"""
QUESTION:
Write a function `is_common_subsequence(s, t, n)` that takes two strings `s` and `t` and an integer `n` as input, and returns `True` if there exists a common substring of length at least `n` between `s` and `t`, and `False` otherwise. The function should have a time complexity of O(n*m), where `n` and `m` are the lengths of `s` and `t` respectively.
"""

def is_common_subsequence(s, t, n):
    len_s = len(s)
    len_t = len(t)
    
    # Initialize a dynamic programming table
    dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]
    
    for i in range(1, len_s + 1):
        for j in range(1, len_t + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] >= n:
                    return True
            else:
                dp[i][j] = 0
                
    return False