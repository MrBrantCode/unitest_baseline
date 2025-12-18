"""
QUESTION:
Write a function `longest_common_substring(s1, s2)` that returns the length of the longest common substring between two strings `s1` and `s2`, along with the substring itself. The function should have a time complexity of O(N*M), where N and M are the lengths of `s1` and `s2` respectively.
"""

def longest_common_substring(s1, s2):
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