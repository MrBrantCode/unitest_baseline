"""
QUESTION:
Implement a function called `levenshtein_distance(s1, s2)` that calculates the minimum number of operations (deletions, insertions, or replacements) needed to transform string `s1` into string `s2`. The function should work for any two input strings `s1` and `s2`.
"""

def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        newDistances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1 + 1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]