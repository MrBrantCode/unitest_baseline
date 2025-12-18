"""
QUESTION:
Create a function `reverse_string` that takes a string as input and returns the reversed string without using any built-in string reversal functions or methods and without using any loops.
"""

def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]