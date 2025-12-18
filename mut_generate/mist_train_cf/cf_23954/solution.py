"""
QUESTION:
Write a function `longest_substring(s1, s2)` that takes two strings `s1` and `s2` as input and returns the longest common substring between them. The function should return the longest substring in `s1` that is also a substring of `s2`. If there are multiple longest common substrings, it can return any one of them.
"""

def longest_substring(s1, s2):
    """
    This function finds the longest common substring between two input strings.

    Parameters:
    s1 (str): The first input string.
    s2 (str): The second input string.

    Returns:
    str: The longest substring in `s1` that is also a substring of `s2`.
    """

    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]