"""
QUESTION:
Implement a function named `levenshtein_distance` that takes two strings `str1` and `str2` as input and returns the minimum number of operations (insertions, deletions, and substitutions) required to transform `str1` into `str2`. The function must not use any built-in string manipulation functions or libraries and must have a time complexity of O(n*m), where n and m are the lengths of `str1` and `str2`, respectively.
"""

def levenshtein_distance(str1, str2):
    # Initialize a matrix with zeros
    rows = len(str1) + 1
    cols = len(str2) + 1
    dist = [[0] * cols for _ in range(rows)]

    # Initialize the first row and column
    for i in range(rows):
        dist[i][0] = i
    for j in range(cols):
        dist[0][j] = j

    # Compute the minimum distance
    for i in range(1, rows):
        for j in range(1, cols):
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 1

            dist[i][j] = min(dist[i-1][j] + 1,         # deletion
                             dist[i][j-1] + 1,         # insertion
                             dist[i-1][j-1] + cost)    # substitution

    return dist[rows-1][cols-1]