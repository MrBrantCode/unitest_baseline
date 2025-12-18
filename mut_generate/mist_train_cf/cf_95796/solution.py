"""
QUESTION:
Write a function `is_palindrome` that determines whether a given string is a palindrome or not, considering only alphanumeric characters and ignoring case sensitivity. The function should return `True` if the string is a palindrome and `False` otherwise. The input string can contain any type of characters, but the function should only consider alphanumeric characters while checking for palindrome.
"""

import re

def is_palindrome(string):
    # Convert to lowercase
    string = string.lower()
    
    # Remove non-alphanumeric characters
    string = re.sub('[^a-z0-9]', '', string)
    
    # Check if the resulting string is equal to its reverse
    return string == string[::-1]