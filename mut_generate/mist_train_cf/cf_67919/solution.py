"""
QUESTION:
Write a function named `levenshtein_distance` that takes two strings `word1` and `word2` as input and returns the minimum number of operations (insertions, deletions, and substitutions) required to transform `word1` into `word2`.
"""

def levenshtein_distance(word1, word2):
    size_x = len(word1) + 1
    size_y = len(word2) + 1
    matrix = [[0 for _ in range(size_y)] for _ in range(size_x)]
    
    for x in range(size_x):
        matrix[x][0] = x
    for y in range(size_y):
        matrix[0][y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if word1[x - 1] == word2[y - 1]:
                matrix[x][y] = min(
                    matrix[x - 1][y] + 1,
                    matrix[x - 1][y - 1],
                    matrix[x][y - 1] + 1
                )
            else:
                matrix[x][y] = min(
                    matrix[x - 1][y] + 1,
                    matrix[x - 1][y - 1] + 1,
                    matrix[x][y - 1] + 1
                )
    return matrix[size_x - 1][size_y - 1]