"""
QUESTION:
Implement a function named `get_distance` that calculates the Levenshtein distance between two input strings `str1` and `str2`. The Levenshtein distance is the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into the other. The function should return the calculated Levenshtein distance.
"""

def levenshtein_distance(str1, str2):
    distance_matrix = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    for i in range(len(str1) + 1):
        distance_matrix[i][0] = i
    for j in range(len(str2) + 1):
        distance_matrix[0][j] = j

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
            distance_matrix[i][j] = min(distance_matrix[i - 1][j] + 1,
                                         distance_matrix[i][j - 1] + 1,
                                         distance_matrix[i - 1][j - 1] + cost)

    return distance_matrix[len(str1)][len(str2)]