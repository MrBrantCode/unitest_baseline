"""
QUESTION:
Create a function `longest_rev_common_subseq(str1, str2)` that takes two strings `str1` and `str2` as inputs and returns the longest common subsequence that appears in reverse in both strings. The function should return the subsequence itself, not its length.
"""

def longest_rev_common_subseq(str1, str2):
    n = len(str1)
    m = len(str2)
    str1 = str1[::-1] 
    str2 = str2[::-1]
 
    dp = [[0 for i in range(m + 1)] for i in range(n + 1)]

    res_len = 0  
    end = 0

    for i in range(1, n + 1):        
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

                if dp[i][j] > res_len:
                    res_len = dp[i][j]
                    end = i - 1

    return str1[end - res_len + 1: end + 1]