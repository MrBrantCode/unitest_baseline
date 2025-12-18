"""
QUESTION:
Create a function named `levenshtein_distance` that calculates the minimum number of operations (insertions, deletions, or substitutions) required to transform one string into another using the Levenshtein Distance algorithm. The function should take two strings `str1` and `str2` as input and return the minimum number of operations required to transform `str1` into `str2`.
"""

def levenshtein_distance(str1, str2):
    matrix = [[0 for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]

    for x in range(len(str1) + 1):
        matrix [x][0] = x
    for y in range(len(str2) + 1):
        matrix [0][y] = y

    for x in range(1, len(str1) + 1):
        for y in range(1, len(str2) + 1):
            if str1[x-1] == str2[y-1]:
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

    return matrix[len(str1)][len(str2)]