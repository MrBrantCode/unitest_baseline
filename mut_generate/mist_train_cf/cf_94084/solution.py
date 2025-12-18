"""
QUESTION:
Write a function `reverse_string(s)` that takes a string `s` as input and returns its reverse without using any built-in string manipulation methods, loops, or explicit recursion. The function should have a time complexity of O(n), where n is the length of the string.
"""

def entance(s):
    if len(s) <= 1:
        return s
    first_char = s[0]
    reversed_substring = entance(s[1:])
    return reversed_substring + first_char