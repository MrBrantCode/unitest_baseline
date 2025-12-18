"""
QUESTION:
Create a function called `is_palindrome` that takes a string as input. The function should determine whether the input string is a palindrome, considering only alphanumeric characters, ignoring case sensitivity, non-alphanumeric characters, and whitespace characters. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

import re

def is_palindrome(string):
    # Remove non-alphanumeric characters
    modified_string = re.sub(r'[^a-zA-Z0-9]', '', string)

    # Convert to lowercase
    modified_string = modified_string.lower()

    # Compare with reverse
    return modified_string == modified_string[::-1]