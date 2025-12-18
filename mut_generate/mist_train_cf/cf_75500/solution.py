"""
QUESTION:
Create a function `check_same_chars` that takes two strings `s1` and `s2` as arguments and returns `True` if the two strings contain the same characters in the same quantities, and `False` otherwise. The function should be case sensitive, treating uppercase and lowercase characters as distinct entities.
"""

def check_same_chars(s1, s2):
    return sorted(s1) == sorted(s2)