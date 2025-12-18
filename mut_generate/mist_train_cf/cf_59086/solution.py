"""
QUESTION:
Implement a function `check_palindrome` that takes a string as input, reverses its order, and checks whether it's a palindrome, ignoring case sensitivity, punctuation, and white spaces. The function should return a boolean value indicating whether the input string is a palindrome or not.
"""

import re

def check_palindrome(text):
    text = re.sub(r'\W+', '', text).lower()
    return text == text[::-1]