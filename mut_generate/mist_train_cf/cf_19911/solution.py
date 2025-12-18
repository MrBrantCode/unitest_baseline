"""
QUESTION:
Write a function `is_palindrome(string)` that determines if a given string is a palindrome. A palindrome is a sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization, but considering non-alphabetic characters as part of the palindrome if they are in the original input string. The function should return True if the string is a palindrome, and False otherwise.
"""

import re

def entrance(string):
    # Remove spaces and punctuation
    clean_string = re.sub(r'[^a-zA-Z0-9]', '', string)
    # Convert to lowercase
    clean_string = clean_string.lower()
    # Compare characters
    for i in range(len(clean_string) // 2):
        if clean_string[i] != clean_string[-i - 1]:
            return False
    return True