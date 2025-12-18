"""
QUESTION:
Create a function named `first_non_space_char` that takes a string as an argument and returns the first non-space character of the string in upper case. If the input is empty or contains only spaces, the function should return `None`.
"""

def first_non_space_char(string):
    stripped = string.strip()
    if not stripped:
        return None
    else:
        return stripped[0].upper()