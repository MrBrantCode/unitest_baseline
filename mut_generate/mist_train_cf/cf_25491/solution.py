"""
QUESTION:
Create a function called `get_even_indexed_chars` that takes a string as input and returns a new string containing all the characters at even indices from the input string. The function should not modify the original string and should be able to handle strings of any length.
"""

def get_even_indexed_chars(s):
    """Return a new string containing all the characters at even indices from the input string."""
    return s[::2]