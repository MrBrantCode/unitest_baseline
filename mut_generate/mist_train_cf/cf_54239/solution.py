"""
QUESTION:
Create a Python function named `clean_and_reverse` that takes a string `s` as input, removes all non-alphanumeric characters, and returns the resulting string in reverse order. Do not use any built-in string functions or the `re` module.
"""

def clean_and_reverse(s):
    new_string = ""
    for char in s:
        if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or (char >= '0' and char <= '9'):
            new_string = char + new_string
    return new_string