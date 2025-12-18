"""
QUESTION:
Write a function `is_palindrome(s: str) -> bool` to detect if a given string is a palindrome or not, considering only alphanumeric characters and ignoring cases. The function should be able to handle input strings having special characters and white spaces. Return `True` if the string is a palindrome, `False` otherwise.
"""

def is_palindrome(s: str) -> bool:
    s = ''.join(ch for ch in s if ch.isalnum()).lower()
    return s == s[::-1]