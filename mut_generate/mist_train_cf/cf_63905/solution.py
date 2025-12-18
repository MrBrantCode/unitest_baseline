"""
QUESTION:
Design a function `is_palindrome(s)` that takes a string `s` as input and returns a Boolean value indicating whether the string is a palindrome, ignoring non-alphanumeric characters and case differences. The function should return `True` if the string is the same when its characters are reversed, and `False` otherwise.
"""

def is_palindrome(s):
    # Removing any non-alphanumeric characters
    s = ''.join(char for char in s if char.isalnum())
    # Converting to lowercase for case insensitive comparison
    s = s.lower()
    # Checking if the string is equal to its reverse
    return s == s[::-1]