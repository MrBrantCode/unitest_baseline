"""
QUESTION:
Create a function `is_panagram(s)` that checks if a given string `s` is a pangram, meaning it contains every letter in the English alphabet. The function should be case-insensitive and should ignore non-alphabetic characters.
"""

def is_panagram(s):
    s = ''.join(c for c in s if c.isalpha())
    return len(set(s.lower())) == 26