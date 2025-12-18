"""
QUESTION:
Write a function `substring_indices(s1, s2)` that takes two strings `s1` and `s2` as input and returns the starting and ending indices of `s2` in `s1` if `s2` is a substring of `s1`. The function should be case insensitive and should not use any built-in substring or contains methods. If `s2` is not a substring of `s1`, the function should return "No substring match found". If `s2` is longer than `s1`, the function should return "Invalid Input".
"""

def substring_indices(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    len1 = len(s1)
    len2 = len(s2)
    if len1 < len2:
        return "Invalid Input"
    for i in range(len1 - len2 + 1):
        if s1[i:i+len2] == s2:
            return (i, i+len2 - 1) # Corrected the end index
    return "No substring match found"