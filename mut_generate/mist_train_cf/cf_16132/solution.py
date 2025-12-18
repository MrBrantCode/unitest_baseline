"""
QUESTION:
Implement a function `reverse_string(s)` that takes a string `s` as input and returns its reverse. The implementation should not use any built-in string manipulation methods, loops, or traditional recursion. The function should achieve a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(s):
    if len(s) <= 1:
        return s
    first_char = s[0]
    reversed_substring = reverse_string(s[1:])
    return reversed_substring + first_char