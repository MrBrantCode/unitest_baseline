"""
QUESTION:
Write a function named `longest_common_subsequence` that takes two distinct textual strings `string1` and `string2` as input and returns the length of the longest shared subsequence of characters within them.
"""

def longest_common_subsequence(string1, string2):
    # Initialize the matrix
    matrix = [[0 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]

    # Iterate through the strings
    for i, char1 in enumerate(string1):
        for j, char2 in enumerate(string2):
            # If characters match
            if char1 == char2:
                matrix[i + 1][j + 1] = matrix[i][j] + 1
            # If characters don't match
            else:
                matrix[i + 1][j + 1] = max(matrix[i + 1][j], matrix[i][j + 1])

    return matrix[-1][-1]