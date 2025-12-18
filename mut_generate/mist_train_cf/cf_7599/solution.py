"""
QUESTION:
Write a function called `is_palindrome` that takes a string `s` as input. The function should determine whether `s` is a palindrome, ignoring non-alphanumeric characters, and considering the input as case-insensitive. It should also handle multi-line input and Unicode characters. The function should return `True` if the input is a palindrome and `False` otherwise. The time complexity of the solution should be O(n), where n is the length of the input string, and the space complexity should be O(1).
"""

import unicodedata

def is_palindrome(s):
    # Normalize the string by removing diacritic marks and converting to lowercase
    normalized = unicodedata.normalize('NFKD', s).encode('ASCII', 'ignore').decode().lower()
    
    # Remove non-alphanumeric characters
    alphanumeric = ''.join(char for char in normalized if char.isalnum())
    
    # Check if the string is a palindrome
    return alphanumeric == alphanumeric[::-1]