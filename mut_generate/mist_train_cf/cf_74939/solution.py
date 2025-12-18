"""
QUESTION:
Write a function `longest_common_subsequence(s1, s2)` that finds the lengthiest mutually occurring sequence of characters between two strings `s1` and `s2`. The function should return this lengthiest mutually occurring sequence.
"""

def longest_common_subsequence(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    lengths = [[0 for _ in range(len_s2+1)] for _ in range(len_s1+1)]
    longest = 0
    row_longest = 0

    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i-1] == s2[j-1]:
                lengths[i][j] = lengths[i-1][j-1] + 1
                if lengths[i][j] > longest:
                    longest = lengths[i][j]
                    row_longest = i
            else:
                lengths[i][j] = 0

    longest_subsequence = s1[row_longest-longest: row_longest]

    return longest_subsequence