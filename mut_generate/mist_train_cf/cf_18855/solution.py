"""
QUESTION:
Implement a function `levenshtein_distance(s1, s2)` that calculates the minimum number of single-character edits (insertions, deletions, or substitutions) necessary to transform string `s1` into string `s2`. The function should handle strings of up to 100 characters in length and have a time complexity of O(n^2) or better. If either string exceeds the length limit, return -1.
"""

def levenshtein_distance(s1, s2):
    """
    Calculate the minimum number of single-character edits (insertions, deletions, or substitutions) 
    necessary to transform string `s1` into string `s2`.

    Args:
    s1 (str): The original string.
    s2 (str): The target string.

    Returns:
    int: The minimum number of single-character edits. Returns -1 if either string exceeds the length limit of 100.
    """

    m = len(s1)
    n = len(s2)
    if m == 0:
        return n
    if n == 0:
        return m
    if m > 100 or n > 100:
        return -1

    d = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = 1 + min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1])
    return d[m][n]