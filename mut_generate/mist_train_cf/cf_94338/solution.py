"""
QUESTION:
Write a function `is_palindrome(s)` that checks if a given string `s` is a palindrome, ignoring special characters and considering alphanumeric characters only. The function should be case-insensitive and handle strings with multiple words and spaces.
"""

def is_palindrome(s):
    """
    Checks if a given string `s` is a palindrome, ignoring special characters 
    and considering alphanumeric characters only. The function is case-insensitive 
    and handles strings with multiple words and spaces.

    Args:
        s (str): The input string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove special characters and convert to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]