"""
QUESTION:
Write a function `levenshtein_distance(s1, s2)` that takes two strings `s1` and `s2` as input and returns the minimum number of single-character edits (insertions, deletions, or substitutions) required to change `s1` into `s2`.
"""

def levenshtein_distance(s1, s2):
    matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        matrix[i][0] = i
    for j in range(len(s2) + 1):
        matrix[0][j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j] + 1, 
                                   matrix[i][j - 1] + 1, 
                                   matrix[i - 1][j - 1] + 1)

    return matrix[len(s1)][len(s2)]