"""
QUESTION:
Write a function `is_palindrome` that takes a string as input and returns a boolean value indicating whether the string is a palindrome or not, without using any built-in string manipulation functions or methods. The comparison should be case-insensitive and should ignore non-alphanumeric characters.
"""

def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left, right = left + 1, right - 1
    return True