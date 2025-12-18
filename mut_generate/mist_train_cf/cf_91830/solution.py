"""
QUESTION:
Write a Python function `longest_common_subsequence(str1, str2)` that takes two strings `str1` and `str2` as input and returns the length of the longest common subsequence between them. The function should be able to handle any two input strings.
"""

def entance(str1, str2):
    # Create a 2D matrix to store the lengths of common subsequences
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Populate the matrix by comparing characters of str1 and str2
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Return the length of the longest common subsequence
    return dp[m][n]