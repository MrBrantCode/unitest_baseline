"""
QUESTION:
Write a function `concat_strings(s1, s2, n, m)` that takes two strings `s1` and `s2` and two integers `n` and `m` as input. The function should return a string that is the concatenation of `s1` and `s2`, repeated `n` times, with the first `m` characters of `s1` capitalized. If either `s1` or `s2` is an empty string, or if `n` or `m` is negative, the function should return an empty string.
"""

def concat_strings(s1, s2, n, m):
    if s1 == "" or s2 == "" or n < 0 or m < 0:
        return ""
    
    s1_capitalized = s1[:m].upper() + s1[m:]
    concatenated = (s1_capitalized + s2) * n
    return concatenated