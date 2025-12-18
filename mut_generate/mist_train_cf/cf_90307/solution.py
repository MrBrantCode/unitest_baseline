"""
QUESTION:
Implement the `levenshtein_distance` function, which calculates the minimum number of operations (insertions, deletions, and substitutions) required to transform one string into another. The function should have a time complexity of O(n*m) and a space complexity of O(min(n, m)), where n and m are the lengths of the two input strings.
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