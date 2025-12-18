"""
QUESTION:
Write a function `unique_chars_in_string(s1, s2)` that takes two strings `s1` and `s2` as input and returns a new string containing the alphabetic characters present only in `s1`, ignoring duplicates and case sensitivity, sorted in ascending order. The function should exclude any non-alphabetic characters and characters present in `s2`.
"""

def unique_chars_in_string(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    unique_chars = set()
    for c in s1:
        if c.isalpha() and c not in s2 and c not in unique_chars:
            unique_chars.add(c)

    return ''.join(sorted(list(unique_chars)))