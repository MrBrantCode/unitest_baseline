"""
QUESTION:
Write a function `longest_common_palindrome_subsequence(str1, str2)` that takes two strings `str1` and `str2` as input and returns the length of their longest common subsequence that is both a palindrome and a substring of both input strings.
"""

def longest_common_palindrome_subsequence(str1, str2):
    n = len(str1)
    m = len(str2)
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    palindrome = [[False] * (m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if palindrome[i-1][j-1] or dp[i][j] == 1:
                    palindrome[i][j] = True
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    lcs = ""
    i, j = n, m
    
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1] and palindrome[i][j]:
            lcs = str1[i-1] + lcs
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return len(lcs)