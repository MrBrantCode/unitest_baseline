"""
QUESTION:
Write a function named `longest_common_subsequence` that takes two string parameters, `s1` and `s2`, and returns the length and all possible longest common subsequences between the two strings. The function should handle cases where there are multiple longest common subsequences and return all of them.
"""

def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    
    # Initialize the matrix
    matrix = [[0] * (n+1) for _ in range(m+1)]
    
    # Compute the lengths of the longest common subsequences
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    
    # Backtrack to find the actual subsequences
    subsequences = []
    current_subsequence = []
    backtrack(matrix, s1, s2, m, n, current_subsequence, subsequences)
    
    return matrix[m][n], subsequences


def backtrack(matrix, s1, s2, i, j, current_subsequence, subsequences):
    if i == 0 or j == 0:
        subsequences.append(''.join(current_subsequence[::-1]))
        return
    
    if s1[i-1] == s2[j-1]:
        current_subsequence.append(s1[i-1])
        backtrack(matrix, s1, s2, i-1, j-1, current_subsequence, subsequences)
        current_subsequence.pop()
    else:
        if matrix[i-1][j] >= matrix[i][j-1]:
            backtrack(matrix, s1, s2, i-1, j, current_subsequence, subsequences)
        
        if matrix[i][j-1] >= matrix[i-1][j]:
            backtrack(matrix, s1, s2, i, j-1, current_subsequence, subsequences)