"""
QUESTION:
Create a function `longest_common_subsequence(str1, str2)` that takes two strings `str1` and `str2` as input and returns the longest common subsequence between the two strings. The subsequence should only contain alphabetical characters. Both input strings should have a minimum length of 5 characters. The function should return the longest common subsequence as a string.
"""

def longest_common_subsequence(str1, str2):
    # Create a 2D matrix to store the lengths of the common subsequences
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    # Iterate through the strings and fill the matrix
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1].isalpha() and str2[j - 1].isalpha():  # Check if characters are alphabetical
                if str1[i - 1] == str2[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                else:
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    # Find the longest common subsequence by backtracking through the matrix
    lcs = ''
    i, j = len(str1), len(str2)
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs
            i -= 1
            j -= 1
        elif matrix[i - 1][j] > matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs