"""
QUESTION:
Write a function `reorder_string` that takes a string as input, removes any duplicate characters, and reorders the remaining characters alphabetically, considering the case of the letters. The function should return the reordered string.
"""

def reorder_string(s):
    return ''.join(sorted(set(s.lower())))