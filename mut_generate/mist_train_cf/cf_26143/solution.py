"""
QUESTION:
Create a function named `levenshtein(word1, word2)` that calculates the Levenshtein distance between two input words `word1` and `word2`. The Levenshtein distance is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.
"""

def levenshtein(word1, word2):
    """Calculate the Levenshtein distance between two words"""
    size_x = len(word1) + 1
    size_y = len(word2) + 1
    matrix = [[0 for i in range(size_x)] for j in range(size_y)] 
    for x in range(size_x):
        matrix[0][x] = x
    for y in range(size_y):
        matrix[y][0] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if word1[x-1] == word2[y-1]:
                matrix[y][x] = min(
                    matrix[y-1][x] + 1,
                    matrix[y-1][x-1],
                    matrix[y][x-1] + 1
                )
            else:
                matrix[y][x] = min(
                    matrix[y-1][x] + 1,
                    matrix[y-1][x-1] + 1,
                    matrix[y][x-1] + 1
                )

    return matrix[size_y-1][size_x-1]