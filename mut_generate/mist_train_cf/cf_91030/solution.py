"""
QUESTION:
Write a function `is_palindrome` that takes a string `s` as input and returns True if it is a palindrome while ignoring non-alphanumeric characters and considering case sensitivity, and False otherwise.
"""

def is_palindrome(s):
    clean_string = ''.join(ch for ch in s if ch.isalnum())
    return clean_string == clean_string[::-1]