"""
QUESTION:
Create a function called `is_palindrome` that determines if a given string is a palindrome. The function should ignore leading or trailing spaces, consider both uppercase and lowercase characters, and only account for alphabetic characters. The input string should not exceed 100 characters in length.
"""

def is_palindrome(s):
    """
    Checks if a given string is a palindrome.

    Args:
    s (str): The input string.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """

    # Removing leading and trailing spaces
    s = s.strip()
    
    # Converting the string to lowercase
    s = s.lower()
    
    # Removing non-alphabetic characters
    s = ''.join(ch for ch in s if ch.isalpha())
    
    # Checking if the string is a palindrome
    return s == s[::-1]