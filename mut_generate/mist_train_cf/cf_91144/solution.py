"""
QUESTION:
Write a function called `string_length` that takes a string `s` as input and returns its length without using the built-in `len()` function or any looping constructs (such as for, while, etc.). The function should be able to handle strings of any length.
"""

def string_length(s):
    if s == '':
        return 0
    else:
        return 1 + string_length(s[1:])