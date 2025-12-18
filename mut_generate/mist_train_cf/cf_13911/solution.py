"""
QUESTION:
Write a function `find_max_length_subsequence` that takes two strings as input and returns the maximum length of their common subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""

def find_max_length_subsequence(string1, string2):
    m = len(string1)
    n = len(string2)
    
    # Create a matrix to store the lengths of common subsequences
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Fill the matrix using dynamic programming approach
    for i in range(1, m+1):
        for j in range(1, n+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # The maximum length of common subsequence is the last element of the matrix
    return dp[m][n]