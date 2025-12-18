"""
QUESTION:
Write a function called `string_length` that takes a string `s` as input and returns the length of the string without using the built-in `len()` function or any looping constructs.
"""

def string_length(s):
    if s == '':
        return 0
    else:
        return 1 + string_length(s[1:])