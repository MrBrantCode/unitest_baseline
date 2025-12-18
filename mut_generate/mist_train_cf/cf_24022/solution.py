"""
QUESTION:
Write a function called `get_uppercase_letters` that takes a string as input and returns a new string containing all the uppercase letters from the input string. The order of the uppercase letters in the new string should match the order they appear in the input string.
"""

def get_uppercase_letters(s):
    return ''.join(c for c in s if c.isupper())