"""
QUESTION:
Construct a function `longest_common_subsequence(s1, s2)` that returns the length and all possible subsequences of the longest common subsequence between two input strings `s1` and `s2`. The function should handle cases with multiple longest common subsequences and non-continuous subsequences. The function should not include any characters not present in the original strings.
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
    def backtrack(i, j):
        if i == 0 or j == 0:
            subsequences.append(''.join(current_subsequence[::-1]))
            return
        
        if s1[i-1] == s2[j-1]:
            current_subsequence.append(s1[i-1])
            backtrack(i-1, j-1)
            current_subsequence.pop()
        else:
            if matrix[i-1][j] >= matrix[i][j-1]:
                backtrack(i-1, j)
            
            if matrix[i][j-1] >= matrix[i-1][j]:
                backtrack(i, j-1)
                
    backtrack(m, n)
    
    return matrix[m][n], subsequences