"""
QUESTION:
Implement a function `one_edit_away(s1, s2)` that checks if two input strings `s1` and `s2` are one edit away from each other, where an edit is an insertion, removal, or replacement of a single character. The function should return `True` if the strings are one edit away, and `False` otherwise.
"""

def one_edit_away(s1, s2):
    len_diff = abs(len(s1) - len(s2))
    if len_diff > 1:
        return False
    elif len_diff == 0:
        replacement_found = False
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if replacement_found:
                    return False
                replacement_found = True
        return True
    else:
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        insertion_found = False
        i = j = 0
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                if insertion_found:
                    return False
                insertion_found = True
                j += 1
            else:
                i += 1
                j += 1
        return True