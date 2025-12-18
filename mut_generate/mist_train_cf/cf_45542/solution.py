"""
QUESTION:
Write a function `alternate_case(s)` that takes a string `s` as input and returns a new string where the case of each letter is alternated, starting with uppercase.
"""

def alternate_case(s):
    """Switch cases in a string."""
    return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s))