"""
QUESTION:
Write a function `find_mismatches(s1, s2)` that takes two strings `s1` and `s2` as input and returns a list of indices where the characters in `s1` and `s2` do not match. If one string is longer than the other, treat every subsequent character in the longer string as a mismatch. The function should return an empty list if there are no mismatches. The comparison must be implemented from scratch without using built-in comparison or diff tools.
"""

def find_mismatches(s1, s2):
    mismatches = []
    # Normalize the length by padding shorter string with None
    maxlen = max(len(s1), len(s2))
    s1 += '\0' * (maxlen - len(s1))
    s2 += '\0' * (maxlen - len(s2))
    
    # Find mismatches
    for idx, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            mismatches.append(idx)
    return mismatches