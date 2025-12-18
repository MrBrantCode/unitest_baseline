"""
QUESTION:
Write a function `remove_first_o` that takes a string as input, removes the first occurrence of 'o' (case-sensitive), and returns the resulting string in lowercase.
"""

def remove_first_o(s):
    return s.replace('o', '', 1).lower()