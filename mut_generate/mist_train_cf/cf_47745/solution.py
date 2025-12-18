"""
QUESTION:
Write a function `palindrome_check(str1, str2)` that takes two string parameters and returns `True` if `str1` is a palindrome of `str2`, considering the case sensitivity, and `False` otherwise.
"""

def is_palindrome(str1, str2):
    return str1[::-1] == str2