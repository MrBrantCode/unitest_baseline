"""
QUESTION:
Create a function `longest_common_subsequence` that takes two strings `s1` and `s2` as input and returns the length of the longest common subsequence between them. The function should use dynamic programming to build a 2D matrix where each cell stores the length of the longest common subsequence up to the corresponding characters in `s1` and `s2`. The function should handle cases where the input strings have different lengths.
"""

def longest_common_subsequence(s1, s2):
    m = len(s1)
    n = len(s2)
    
    # Create a matrix to store the lengths of common subsequences
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Fill in the matrix using dynamic programming
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]