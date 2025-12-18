"""
QUESTION:
Write a function named `is_palindrome` that takes a string `s` as input and returns `True` if the string is a palindrome and `False` otherwise, without using any additional memory space.
"""

def is_palindrome(s):
    return s == s[::-1]