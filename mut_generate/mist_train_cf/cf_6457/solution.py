"""
QUESTION:
Write a function `reverse_string(s)` that takes a string `s` of alphanumeric characters with a maximum length of 100 characters as input, reverses it using recursion, and returns the reversed string with a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return reverse_string(s[1:]) + s[0]