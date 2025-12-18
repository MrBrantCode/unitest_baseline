"""
QUESTION:
Write a function `repeat_strings` that takes two strings `s1` and `s2`, and an integer `n`, and returns a string that is the concatenation of `s1` and `s2` repeated `n` times. If either `s1` or `s2` is an empty string, or if `n` is negative, return an empty string.
"""

def repeat_strings(s1: str, s2: str, n: int) -> str:
    if s1 == "" or s2 == "" or n < 0:
        return ""
    return (s1 + s2) * n