"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns a single string composed of all the characters of the input string in reverse order. You must not use any built-in string reversal functions or methods.
"""

def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])