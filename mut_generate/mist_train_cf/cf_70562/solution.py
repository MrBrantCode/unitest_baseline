"""
QUESTION:
Write a function `is_palindrome(text)` that takes a string as input and returns `True` if the string is a palindrome, ignoring spaces, punctuation, and capitalization, and `False` otherwise. The function should process the string by removing non-alphanumeric characters and converting it to lowercase before checking if it is a palindrome.
"""

import re

def is_palindrome(text):
    text = re.sub(r'[^\w]', '', text)
    text = text.lower()
    return text == text[::-1]