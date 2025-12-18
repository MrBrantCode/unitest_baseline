"""
QUESTION:
Write a function `lcs(s1, s2)` that takes two strings `s1` and `s2` as input and returns their longest common subsequence. The function should not use any built-in functions that directly compute the longest common subsequence.
"""

def longestCommonSubsequence(s1, s2):
    m = len(s1)
    n = len(s2)
    
    # Declare the matrix with all entries set to 0
    matrix = [[0 for i in range(n + 1)] for j in range(m + 1)]
    
    # Fill the matrix in bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
                
    # Initialize result string
    result = ''
    
    # Start from the right-most bottom-most corner and one by one store characters in result
    i = m
    j = n
    while i > 0 and j > 0:
        # If current character in s1 and s2 are same, then the character is part of LCS
        if s1[i - 1] == s2[j - 1]:
            result = s1[i - 1] + result
            i -= 1
            j -= 1
        # If not same, then find the larger of two and go in the direction of larger value
        elif matrix[i - 1][j] > matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    return result