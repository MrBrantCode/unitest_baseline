"""
QUESTION:
Create a function `is_palindrome` that determines if a given string is a palindrome without using any built-in string manipulation functions or methods and without using any extra data structures. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True