"""
QUESTION:
Write a function called "longest_common_subsequence" that takes in two strings, a and b, and returns the length of the longest common subsequence, which is defined as the longest sequence of characters that appear in the same order in both strings, but not necessarily consecutively. The function should have a time complexity of O(m*n), where m and n are the lengths of strings a and b, respectively.
"""

def longest_common_subsequence(a, b):
    m = len(a)
    n = len(b)
    
    # Create a matrix to store the lengths of longest common subsequences
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Compute the lengths of longest common subsequences
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Return the length of the longest common subsequence
    return dp[m][n]