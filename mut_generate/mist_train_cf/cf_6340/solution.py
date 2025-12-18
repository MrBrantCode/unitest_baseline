"""
QUESTION:
Write a function called `levenshteinDistance` that calculates the Levenshtein distance between two input strings `str1` and `str2`, both containing only lowercase alphabetical characters. Implement the function using a dynamic programming approach with memoization, achieving a time complexity of O(m*n) and a space complexity of O(min(m,n)), where m and n are the lengths of the input strings.
"""

def levenshteinDistance(str1, str2):
    # Calculate the lengths of the input strings
    m = len(str1)
    n = len(str2)
    
    # Create the matrix to store the Levenshtein distances
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Initialize the first row and column of the matrix
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    
    # Fill in the rest of the matrix using dynamic programming
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    # Return the Levenshtein distance between the two strings
    return dp[m][n]