"""
QUESTION:
Write a function `is_palindrome(word)` that checks whether a given word is a palindrome or not, ignoring spaces, punctuation, and capitalization. The function should return `True` if the word is a palindrome, and `False` otherwise.
"""

import re

def entrance(word):
    word = re.sub('[^a-zA-Z0-9]', '', word.lower())
    return word == word[::-1]