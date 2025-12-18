"""
QUESTION:
Implement a function `levenshtein_distance(word1, word2)` that calculates the Levenshtein distance between two input words `word1` and `word2`. The Levenshtein distance is the minimum number of operations (insertions, deletions, and substitutions) required to transform `word1` into `word2`. Do not use any built-in string manipulation functions or libraries.
"""

def entrance(word1, word2):
    m, n = len(word1), len(word2)
    # Create a matrix of size (m+1)x(n+1) to store the distances
    distance = [[0] * (n+1) for _ in range(m+1)]

    # Initialize the first row and column of the matrix
    for i in range(m+1):
        distance[i][0] = i
    for j in range(n+1):
        distance[0][j] = j

    # Fill in the rest of the matrix using dynamic programming
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                cost = 0
            else:
                cost = 1
            distance[i][j] = min(distance[i-1][j] + 1, distance[i][j-1] + 1, distance[i-1][j-1] + cost)

    return distance[m][n]