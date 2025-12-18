"""
QUESTION:
Write a function called `levenshtein_distance` that takes two strings as input and returns the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into another. The function should not take any additional parameters besides the two strings.
"""

def levenshtein_distance(s1, s2):
    # Create a matrix with dimensions len(s1)+1 x len(s2)+1
    matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Initialize the first row and column of the matrix
    for i in range(len(s1) + 1):
        matrix[i][0] = i
    for j in range(len(s2) + 1):
        matrix[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            # If the characters at the current positions are equal, no edit is needed
            if s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                # Otherwise, find the minimum of the three possible edits: insertion, deletion, and substitution
                matrix[i][j] = min(matrix[i - 1][j] + 1,      # deletion
                                   matrix[i][j - 1] + 1,      # insertion
                                   matrix[i - 1][j - 1] + 1)  # substitution

    # The final value in the bottom-right corner of the matrix is the Levenshtein distance
    return matrix[len(s1)][len(s2)]