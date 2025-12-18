"""
QUESTION:
Create a function named `minimal_replacements` that takes two strings `s1` and `s2` as input. The function should return the minimal number of replacements required to make `s1` equal to `s2` by replacing characters in `s1` with the corresponding characters in `s2`, where asterisks in `s2` can represent any character. The function should be able to handle strings containing any Unicode characters.
"""

def minimal_replacements(s1, s2):
    i = 0
    j = 0
    replacements = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j] or s2[j] == '*':
            i += 1
            j += 1
        elif s1[i] != s2[j]:
            replacements += 1
            i += 1
    return replacements