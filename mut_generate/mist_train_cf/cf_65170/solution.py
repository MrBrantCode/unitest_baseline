"""
QUESTION:
Write a function `compare` that sorts a list of strings in alphabetical order with case sensitivity. If two strings are identical, order them by length. The function should take two string arguments and return a boolean value indicating whether the first string should come before the second string in the sorted list.
"""

def compare(s1, s2):
    if s1 != s2:
        return s1 < s2
    return len(s1) < len(s2)