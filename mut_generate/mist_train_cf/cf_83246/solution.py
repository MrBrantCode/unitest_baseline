"""
QUESTION:
Write a function called `is_palindrome` that determines if a given string is a palindrome, ignoring case, punctuation, and spacing. The function should handle strings of varying lengths efficiently.
"""

import re

def is_palindrome(s):
    # Remove punctuation and spaces
    simplified_string = re.sub(r'\W+', '', s)

    # Ignore case
    simplified_string = simplified_string.lower()

    # Compare the string and its reverse
    return simplified_string == simplified_string[::-1]