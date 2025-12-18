"""
QUESTION:
Write a function named `is_reverse_string` that takes two strings as input and returns `True` if one string is the reverse of the other. The function should handle strings containing special characters, numbers, and whitespace characters. The function should have a time complexity of O(n), where n is the length of the strings, and should not use any built-in string reversal functions or methods. The function should be case insensitive and should ignore whitespace characters, special characters, and numbers in the comparison.
"""

def is_reverse_string(s1, s2):
    s1 = "".join(c for c in s1.lower() if c.isalpha())
    s2 = "".join(c for c in s2.lower() if c.isalpha())
    return s1 == s2[::-1]