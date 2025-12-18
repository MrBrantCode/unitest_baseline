"""
QUESTION:
Write a function `longest_common_subsequence_length` that takes two strings as input and returns the length of the longest common subsequence between the two strings that is also a palindrome. The function should not return the subsequence itself, only its length.
"""

def longest_common_subsequence_length(s1, s2):
    n = len(s1)
    m = len(s2)
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    lcs = ""
    i = n
    j = m
    
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs = s1[i-1] + lcs
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    lcs_is_palindrome = lcs == lcs[::-1]
    
    if lcs_is_palindrome:
        return len(lcs)
    else:
        return 0