"""
QUESTION:
Implement a function `check_descending(s)` that takes a string `s` as input and returns `True` if the characters in `s` are in lexicographically descending order, and `False` otherwise. The input string `s` is assumed to be a non-empty string consisting only of lowercase English alphabet letters.
"""

def check_descending(s):
    for i in range(1, len(s)):
        if s[i] > s[i-1]:
            return False
    return True