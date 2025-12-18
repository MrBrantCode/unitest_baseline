"""
QUESTION:
Write a Python function called `reverse_str` that uses recursion to reverse a given string `s`. The function should work for both ASCII and Unicode strings. The function should return the reversed string. The time complexity of the function should be documented for strings of different lengths.
"""

def reverse_str(s):
    if len(s) == 0:
        return s
    else:
        return reverse_str(s[1:]) + s[0]