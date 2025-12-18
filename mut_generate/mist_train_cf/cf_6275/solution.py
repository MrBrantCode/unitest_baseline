"""
QUESTION:
Write a function named `reverse_and_convert` that takes a string as input and returns the string in reverse order with all uppercase letters converted to lowercase and all lowercase letters converted to uppercase, while removing any punctuation marks or special characters. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

import string

def reverse_and_convert(s):
    return ''.join(c.swapcase() for c in s if c.isalnum())[::-1]