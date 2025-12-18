"""
QUESTION:
Write a function named `longest_common_substring` that takes two strings `str1` and `str2` as input and returns the length of the longest common substring between them. The function should be case-sensitive and consider substrings of any length that appear consecutively in both strings. If there are multiple common substrings of the same maximum length, the function should return the length of the first one encountered. The time complexity of the function should be O(n^2), where n is the length of the input strings, and the auxiliary space complexity should be O(min(m, n)), where m and n are the lengths of the input strings. The function should not use any built-in string comparison or search functions, external libraries or modules, or recursion, and should be implemented using dynamic programming.
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