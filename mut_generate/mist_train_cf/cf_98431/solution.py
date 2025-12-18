"""
QUESTION:
Create a function called `reverse_string` that takes in a string argument and returns the reversed string using recursion.
"""

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]