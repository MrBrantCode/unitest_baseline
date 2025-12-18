"""
QUESTION:
Write a function `is_one_edit_away` that takes two strings `s1` and `s2` as input and returns a boolean value indicating whether `s1` can be transformed into `s2` with a single edit operation (insert, remove, or replace a character). The function should handle strings of different lengths and consider only exact single edit operations.
"""

def is_one_edit_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) == len(s2):
        return sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True