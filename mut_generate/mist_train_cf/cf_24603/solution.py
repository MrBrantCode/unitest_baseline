"""
QUESTION:
Write a function `levenshtein_distance(str1, str2)` that calculates the minimum number of single-character edits (insertions, deletions, or substitutions) necessary to transform `str1` into `str2`. The function should take two strings as input and return the Levenshtein Distance as an integer.
"""

def levenshtein_distance(str1, str2):
    # Create a matrix for storing the distances
    m = [[0 for x in range(len(str2) + 1)] for x in range(len(str1) + 1)]
    # Mark the first Edit Distance value as 0
    m[0][0] = 0

    # Iterate over the matrix 
    for i in range(0, len(str1) + 1):
        for j in range(0, len(str2) + 1):
            # If we are at the first row or first col, mark the cells with corresponding numbers
            if i == 0:
                m[i][j] = j
            elif j == 0:
                m[i][j] = i
            # Otherwise, calculate the distance according to the  formula
            else:
                if str1[i-1] == str2[j-1]:
                    m[i][j] = m[i-1][j-1]
                else:
                    m[i][j] = min(m[i-1][j], m[i-1][j-1], m[i][j-1]) + 1
            
    # Return the last element in the matrix, which is the Levenshtein Distance
    return m[-1][-1]