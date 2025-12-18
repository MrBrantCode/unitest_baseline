"""
QUESTION:
Write a function `unique_chars_in_string(s1, s2)` that returns a new string containing the alphabetic characters present only in string `s1`, ignoring duplicates, case sensitivity, and non-alphabetic characters. The returned string should be sorted in ascending order.
"""

def unique_chars_in_string(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    unique_chars = set()
    for c in s1:
        if c.isalpha() and c not in s2 and c not in unique_chars:
            unique_chars.add(c)

    unique_chars = sorted(list(unique_chars))
    return ''.join(unique_chars)