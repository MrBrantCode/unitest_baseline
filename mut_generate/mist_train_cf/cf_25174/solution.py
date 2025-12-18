"""
QUESTION:
Write a function called `is_palindrome` that determines if a given input string is a palindrome. The function should return a boolean value indicating whether the string is a palindrome or not. The function should be case-insensitive, i.e., it should treat 'A' and 'a' as the same character.
"""

def is_palindrome(string):
    """
    Returns True if the given string is a palindrome, False otherwise.

    The function is case-insensitive, treating 'A' and 'a' as the same character.

    Parameters:
    string (str): The input string to check.

    Returns:
    bool: Whether the string is a palindrome.
    """
    string = string.lower()
    rev_string = string[::-1]
    return string == rev_string