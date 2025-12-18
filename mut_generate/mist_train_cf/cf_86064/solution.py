"""
QUESTION:
Create a function called `find_character` that takes a string `s` and a character `c` as input and returns the index of the first occurrence of `c` in `s`. If `c` is not found in `s`, the function should return -1.
"""

def find_character(s, c):
    return s.index(c) if c in s else -1