"""
QUESTION:
Write a function `is_palindrome(s)` that checks if a given string `s` is a palindrome, i.e., it reads the same backward as forward, and returns a boolean value. The function should be case sensitive and consider spaces and punctuation as part of the string.
"""

def is_palindrome(s):
 """
 Returns True if the given string is a palindrome, False otherwise.
 """
 return s == s[::-1]