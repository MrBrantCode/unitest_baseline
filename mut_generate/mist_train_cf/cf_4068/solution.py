"""
QUESTION:
Implement a function named `levenshtein_distance` that calculates the minimum number of single-character edits (insertions, deletions, or substitutions) necessary to transform one string into another. The function should handle strings of up to 100 characters in length and have a time complexity of O(n^2) or better. It should not use recursion, external libraries, built-in functions, or global variables, and should not modify the input strings. The input strings will only contain lowercase letters.
"""

def levenshtein_distance(str1, str2):
    # Initialize a matrix of size (m+1)x(n+1) where m and n are the lengths of str1 and str2 respectively
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    # Fill the first row and column with values from 0 to m and 0 to n respectively
    for i in range(len(matrix)):
        matrix[i][0] = i
    for j in range(len(matrix[0])):
        matrix[0][j] = j
    
    # Traverse the matrix and fill it with the minimum edit distance values
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            # If the characters at the current positions are the same, the edit distance is the same as the previous positions
            if str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                # Otherwise, the edit distance is the minimum of the values above, left, and top-left + 1
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
    
    # The minimum edit distance is the value at the bottom-right corner of the matrix
    return matrix[-1][-1]