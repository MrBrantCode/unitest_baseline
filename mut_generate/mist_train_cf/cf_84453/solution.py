"""
QUESTION:
Write a function `isValidKPalindromeSubString(s, k, sub)` that takes a string `s`, an integer `k`, and a substring `sub` as input. The function should return `true` if `s` is a `k`-palindrome and contains `sub` as a substring, and `false` otherwise. A string is `k`-palindrome if it can be transformed into a palindrome by removing at most `k` characters from it. The function should assume that `1 <= s.length <= 1000`, `s` consists of only lowercase English letters, `1 <= k <= s.length`, `1 <= sub.length <= s.length`, and `sub` consists of only lowercase English letters.
"""

def isValidKPalindromeSubString(s, k, sub):
    if sub not in s: 
        return False
    
    n = len(s)
    dp = [[0]*n for _ in range(n)]
 
    for gap in range(1, n):
        for i in range(n-gap):
            j = i + gap
    
            if s[i] == s[j]: 
                dp[i][j] = dp[i+1][j-1] if i+1 <= j-1 else 0
            else: 
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1

    return dp[0][n-1] <= k