"""
QUESTION:
Create a function `is_palindrome(s)` that determines whether a given string `s` is a palindrome, ignoring spaces, punctuation, and capitalization. The function should return `True` if the string is a palindrome and `False` otherwise. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def entrance(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]