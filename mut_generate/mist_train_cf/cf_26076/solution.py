"""
QUESTION:
Create a function named `collapse_whitespace` that takes a string as input and returns a string where all consecutive whitespaces are replaced with a single space.
"""

def collapse_whitespace(s):
    return ' '.join(s.split())