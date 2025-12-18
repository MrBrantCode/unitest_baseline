"""
QUESTION:
Implement a function `longest_common_subsequence(str1, str2)` that finds the longest common subsequence between two strings `str1` and `str2`. The function should only consider alphabetical characters and should return an empty string if no common alphabetical characters exist. Both `str1` and `str2` are guaranteed to have a minimum length of 5 characters each.
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