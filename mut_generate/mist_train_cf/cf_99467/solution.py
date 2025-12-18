"""
QUESTION:
Write a recursive function called `reverse_str` that takes a string `s` as input and returns the reversed string. The function should handle strings of any length, including those with Unicode characters. The function's time complexity should be clearly understood and explained.
"""

def reverse_str(s):
    if len(s) == 0:
        return s
    else:
        return reverse_str(s[1:]) + s[0]