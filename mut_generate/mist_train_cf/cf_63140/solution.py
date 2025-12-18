"""
QUESTION:
Create a function named `consolidate_list` that takes a multi-dimensional list of characters as input and returns a string of uninterrupted alphabetic characters. The function should preserve the original sequence of the characters and ignore non-alphabetic characters and spaces.
"""

def consolidate_list(characters):
    return ''.join(c for sublist in characters for c in sublist if c.isalpha())