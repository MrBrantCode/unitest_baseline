"""
QUESTION:
Implement a function `is_palindrome(s)` that takes a string `s` as input and returns `True` if the string is a palindrome (reads the same forward and backward, disregarding spaces, punctuation, and capitalization) and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def entance(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]