"""
QUESTION:
Create a function `is_palindrome(input_string)` that takes a string as input and checks whether it's a palindrome or not. The function should ignore non-alphanumeric characters, be case-insensitive, and consider only the characters a-z, A-Z, and 0-9. Return True if the string is a palindrome and False otherwise.
"""

import re

def is_palindrome(input_string):
    # Regular expression to match strings of a-z, A-Z and 0-9 characters
    matched_string = re.findall('[a-zA-Z0-9]', input_string)

    # Join the matched characters into a string
    refined_string = "".join(matched_string).lower()

    # Check if the string is a palindrome
    return refined_string == refined_string[::-1]