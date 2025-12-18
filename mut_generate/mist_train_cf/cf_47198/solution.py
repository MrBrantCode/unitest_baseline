"""
QUESTION:
Create a function `clean_and_lower_string` that takes a string `s` as input and returns a new string containing only the lowercase alphabetical characters from the original string, excluding any non-alphabetical characters and maintaining the original order.
"""

def clean_and_lower_string(s):
    return "".join(c.lower() for c in s if c.isalpha())