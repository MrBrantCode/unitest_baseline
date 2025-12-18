"""
QUESTION:
Create a function named `is_palindrome` that evaluates whether a given sequence of alphanumeric characters is a palindrome, considering complex Unicode characters and ignoring non-alphanumeric characters. The function should be robust, efficient, and not use built-in palindrome checking functions.
"""

def is_palindrome(s):
    s = ''.join(i for i in s if i.isalnum()).lower()
    return s == s[::-1]