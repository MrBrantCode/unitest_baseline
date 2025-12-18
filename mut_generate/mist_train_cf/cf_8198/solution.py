"""
QUESTION:
Create a function named `reverse_string` that takes a string `s` as input and returns its reverse. The function should not use any built-in string reverse or string manipulation functions and should not use any loops.
"""

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]