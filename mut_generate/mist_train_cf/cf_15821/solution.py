"""
QUESTION:
Implement a function `longest_common_substring(str1, str2)` that takes two input strings `str1` and `str2` and returns the length of the longest common substring between them. The function should be case-sensitive, consider substrings of any length that appear consecutively in both strings, and return the length of the first maximum-length common substring encountered. The function should have a time complexity of O(n^2), where n is the length of the input strings, and an auxiliary space complexity of O(min(m, n)), where m and n are the lengths of the input strings.
"""

def longest_common_substring(str1, str2):
    max_len = 0
    len1 = len(str1)
    len2 = len(str2)
    
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
    
    return max_len