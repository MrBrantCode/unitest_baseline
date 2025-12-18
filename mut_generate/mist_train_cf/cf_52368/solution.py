"""
QUESTION:
Write a function `isPalindrome(s)` that takes a string `s` as input and returns `True` if the string is a palindrome (ignoring case sensitivity and spaces) and `False` otherwise.
"""

def isPalindrome(s):
    """
    Returns True if the input string is a palindrome (ignoring case sensitivity and spaces), False otherwise.

    :param s: Input string
    :return: Boolean indicating whether the string is a palindrome
    """
    s = s.replace(' ', '').lower()
    return s == s[::-1]