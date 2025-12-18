"""
QUESTION:
Create a function named `is_palindrome` that takes a string as input. The function should return `True` if the input string is a palindrome, ignoring non-alphabetic characters and whitespace, and considering only lowercase alphabetic characters. Otherwise, it should return `False`.
"""

def is_palindrome(s):
    # Remove non-alphabetic characters and convert to lowercase
    clean_string = ''.join(char.lower() for char in s if char.isalpha())

    # Check if the clean string is equal to its reverse
    return clean_string == clean_string[::-1]