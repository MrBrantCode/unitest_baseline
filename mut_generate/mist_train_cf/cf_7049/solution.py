"""
QUESTION:
Implement a recursive function `reverse_string(s)` that takes a string `s` as input and returns the reversed string. The function should have a time complexity of O(n^2) and a space complexity of O(n), where n is the length of the string. The function should not use any built-in string manipulation functions or data structures, and it should handle strings of any length, including empty strings and non-ASCII characters.
"""

def entance(s):
    if len(s) <= 1:
        return s
    else:
        return entance(s[1:]) + s[0]