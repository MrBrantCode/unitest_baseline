"""
QUESTION:
Implement a function named `jaro_winkler` that calculates the similarity between two strings using the Jaro-Winkler distance algorithm. The function should take two strings `s1` and `s2` as input, and an optional parameter `p` (a scaling factor) that defaults to 0.1. The function should return a score between 0 and 1 indicating the similarity between the two strings, where 1 means the strings are identical and 0 means no similarity at all.
"""

def jaro_winkler(s1, s2, p=0.1):
    """
    :param s1: string 1
    :param s2: string 2
    :param p: scaling factor
    The function calculates Jaro distance and the applies
    the Winkler's modification.
    """
    s1_len = len(s1)
    s2_len = len(s2)

    if s1_len == 0 and s2_len == 0:
        return 1.0

    match_distance = (max(s1_len, s2_len) // 2) - 1

    s1_matches = [False] * s1_len
    s2_matches = [False] * s2_len

    matches = 0
    transpositions = 0

    for i in range(s1_len):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, s2_len)

        for j in range(start, end):
            if s2_matches[j]:
                continue
            if s1[i] != s2[j]:
                continue
            s1_matches[i] = True
            s2_matches[j] = True
            matches += 1
            break

    if matches == 0:
        return 0.0

    k = 0
    for i in range(s1_len):
        if not s1_matches[i]:
            continue
        while not s2_matches[k]:
            k += 1
        if s1[i] != s2[k]:
            transpositions += 1
        k += 1

    score = ((matches / s1_len) +
             (matches / s2_len) +
             ((matches - transpositions / 2) / matches)) / 3

    if score < 0.7:
        return score

    l = min(len(s1[:4]), len(s2[:4]))
    score += l * p * (1 - score)

    return score