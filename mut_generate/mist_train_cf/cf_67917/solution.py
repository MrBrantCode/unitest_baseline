"""
QUESTION:
Develop a function named `levenshtein_distance` that takes two string inputs `s1` and `s2` and returns the Levenshtein distance between them using the Wagner-Fisher algorithm. The function should use dynamic programming to compute the edit distance by creating a 2D matrix and calculating the minimum edit operations (insertions, deletions, or substitutions) required to transform `s1` into `s2`.
"""

def levenshtein_distance(s1, s2):
    size_x = len(s1) + 1
    size_y = len(s2) + 1
    matrix = [[0 for y in range(size_y)] for x in range(size_x)]
    
    for x in range(size_x):
        matrix [x][0] = x
    for y in range(size_y):
        matrix [0][y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if s1[x-1] == s2[y-1]:
                matrix [x][y] = min(
                    matrix[x-1][y] + 1,
                    matrix[x-1][y-1],
                    matrix[x][y-1] + 1
                )
            else:
                matrix [x][y] = min(
                    matrix[x-1][y] + 1,
                    matrix[x-1][y-1] + 1,
                    matrix[x][y-1] + 1
                )
    return matrix[size_x - 1][size_y - 1]