"""
QUESTION:
Write a function `is_palindrome` that determines whether a given string is a palindrome or not. The function should take one argument, the string to be checked, and return a boolean value indicating whether the string is a palindrome. The function should be case-sensitive and consider spaces and punctuation as part of the string.
"""

def is_palindrome(s):
    return s == s[::-1]