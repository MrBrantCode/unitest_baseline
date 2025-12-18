"""
QUESTION:
Find the total number of non-overlapping occurrences of a pattern p in a given string S. The function should be named `count_occurrences` and take two parameters: `S` and `p`, both of which are strings containing only lowercase letters.
"""

def count_occurrences(S, p):
    count = 0
    index = 0
    while index < len(S):
        occurrence_index = S.find(p, index)
        if occurrence_index == -1:
            break
        count += 1
        index = occurrence_index + len(p)
    return count