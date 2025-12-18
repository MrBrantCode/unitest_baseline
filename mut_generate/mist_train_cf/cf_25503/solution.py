"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the reversed string without using any loops. The function should handle strings of any length, including empty strings.
"""

def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return reverse_string(s[1:]) + s[0]