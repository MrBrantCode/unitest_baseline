"""
QUESTION:
Write a function `isKPalindrome(s, k, sub)` that takes a string `s`, an integer `k`, and a substring `sub` as input. The function should return `True` if `s` can be transformed into a palindrome by removing at most `k` characters and contains `sub` as a substring, and `False` otherwise. The function should have a time complexity of O(N^2), where N is the length of `s`. 

Restrictions: `1 <= s.length <= 1000`, `s` and `sub` are composed solely of lowercase English alphabets, `1 <= k <= s.length`, and `1 <= sub.length <= s.length`.
"""

def isKPalindrome(s, k, sub):
    def longestCommonSubsequence(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

    if sub not in s:
        return False
    lcs = longestCommonSubsequence(s, s[::-1])
    if len(s) - lcs > k:
        return False
    return True