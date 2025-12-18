"""
QUESTION:
Write a function `calculate_levenshtein_distance` that takes two strings `str1` and `str2` as input and returns the Levenshtein Distance between them. The Levenshtein Distance is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.
"""

import numpy as np

def levenshtein_distance(str1, str2):    
    distances = np.zeros((len(str1)+1, len(str2)+1))
    for i in range(0, len(str1)+1):
        distances[i, 0] = i
    for j in range(0, len(str2)+1):
        distances[0, j] = j
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                distances[i, j] = distances[i-1, j-1]
            else:
                distances[i, j] = min(distances[i-1, j], distances[i, j-1], distances[i-1, j-1]) + 1
    return distances[len(str1), len(str2)]