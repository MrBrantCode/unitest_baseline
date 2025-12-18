"""
QUESTION:
Implement a function `levenshtein_distance(s1, s2)` that calculates the Levenshtein distance between two strings `s1` and `s2`, representing the minimum number of single-character edits (additions, deletions, or substitutions) required to transform `s1` into `s2`. The function should handle strings of different lengths and return the Levenshtein distance as an integer.
"""

def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]