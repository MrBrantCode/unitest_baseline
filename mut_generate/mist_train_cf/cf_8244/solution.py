"""
QUESTION:
Implement a function called `levenshtein_distance` that calculates the Levenshtein distance between two input strings `str1` and `str2`. The Levenshtein distance is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. 

The function should not use any built-in string manipulation functions or libraries. The function should have a time complexity of O(n*m), where n and m are the lengths of `str1` and `str2`, and a space complexity of O(min(n, m)).
"""

def levenshtein_distance(str1, str2):
    if str1 == str2:
        return 0

    if len(str1) > len(str2):
        str1, str2 = str2, str1

    distances = range(len(str1) + 1)

    for i2, c2 in enumerate(str2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(str1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_

    return distances[-1]