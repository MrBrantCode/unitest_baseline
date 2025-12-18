"""
QUESTION:
Implement the function `min_edit_distance(str1, str2)` to compute the minimum string edit distance between two strings of different lengths. The edit distance is defined as the minimum number of operations required to transform one string into another, where the allowed operations are insertion, deletion, and substitution of a single character. 

The algorithm should have a time complexity of O(m*n), where m and n are the lengths of str1 and str2 respectively. Additionally, the space complexity should be O(min(m, n)). The algorithm should only use dynamic programming approach to solve this problem efficiently.
"""

def min_edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Initialize the matrix M
    M = [[0] * (n+1) for _ in range(m+1)]
    
    # Initialize the first row and column of M
    for i in range(m+1):
        M[i][0] = i
    for j in range(n+1):
        M[0][j] = j
    
    # Calculate the minimum edit distance
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                M[i][j] = M[i-1][j-1]
            else:
                M[i][j] = min(M[i-1][j-1], M[i][j-1], M[i-1][j]) + 1
    
    # Return the minimum edit distance
    return M[m][n]