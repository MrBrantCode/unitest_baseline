"""
QUESTION:
Write a function `reverse_string(s)` that takes a string `s` as input and returns the reversed string without using any in-built Python functions, with a time complexity of O(n) and a space complexity of O(n). Implement the function using a recursive approach.
"""

def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]