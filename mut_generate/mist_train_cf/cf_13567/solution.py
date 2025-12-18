"""
QUESTION:
Write a function `is_palindrome(word)` that determines if a given word is a palindrome, ignoring case sensitivity, punctuation, and white spaces. The function should return a boolean value indicating whether the word is a palindrome or not.
"""

import re

def entrance(word):
    # Remove punctuation and white spaces
    word = re.sub(r'\W+', '', word)

    # Convert the word to lowercase
    word = word.lower()

    # Check if the word is equal to its reversed version
    return word == word[::-1]