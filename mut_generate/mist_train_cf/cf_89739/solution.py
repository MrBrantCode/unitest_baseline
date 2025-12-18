"""
QUESTION:
Write a recursive function called `reverse_string` that takes a string `s` as input and returns the reversed string. The function should handle strings of any length, including empty strings, and non-ASCII characters. It should not use any built-in string manipulation functions, data structures, or loops, and should have a time complexity of O(n^2) and a space complexity of O(n).
"""

def entrance(s):
    if len(s) <= 1:
        return s
    else:
        return entrance(s[1:]) + s[0]