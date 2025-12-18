"""
QUESTION:
Write a function `is_palindrome(string)` that determines whether a given string is a palindrome or not, considering only alphanumeric characters and ignoring case sensitivity and non-alphanumeric characters. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

import re

def is_palindrome(string):
    # Remove non-alphanumeric characters
    modified_string = re.sub(r'[^a-zA-Z0-9]', '', string)

    # Convert to lowercase
    modified_string = modified_string.lower()

    # Compare with reverse
    return modified_string == modified_string[::-1]