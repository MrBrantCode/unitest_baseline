"""
QUESTION:
Create a recursive function called `reverse_str` that takes a string `s` as input and returns the reversed string without using any pre-existing function, iterative construct, or data structure. The function should handle strings of varying lengths, special characters, and spaces accurately.
"""

def reverse_str(s):
    if len(s) == 0:
        return s
    else:
        return reverse_str(s[1:]) + s[0]