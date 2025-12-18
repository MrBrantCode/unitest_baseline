"""
QUESTION:
Write a function `longest_common_substring(strings)` that takes a list of strings as input and returns the longest common substring among all strings in the list. The function should find the longest common substring that is shared by all strings, not just the longest common substring between two strings. The input list contains at least two strings. The function should return an empty string if no common substring exists.
"""

def longest_common_substring(strings):
    def dp(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        max_length = 0
        max_end = 0
        for i in range(m+1):
            for j in range(n+1):
                if i and j and s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
                        max_end = i
        return s1[max_end - max_length: max_end]

    def find_common(strings):
        common = strings[0]
        for string in strings[1:]:
            common = dp(common, string)
        return common

    return find_common(strings)