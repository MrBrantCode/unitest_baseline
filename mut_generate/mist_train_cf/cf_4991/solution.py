"""
QUESTION:
Write a function named 'is_palindrome' that determines whether a given string is a palindrome, ignoring case sensitivity, spaces, and special characters, and achieves a time complexity of O(n).
"""

def is_palindrome(s: str) -> bool:
    """
    This function determines whether a given string is a palindrome, 
    ignoring case sensitivity, spaces, and special characters.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """

    # Convert the string to lowercase
    s = s.lower()
    
    # Remove any special characters and spaces from the string
    s = ''.join(e for e in s if e.isalnum())
    
    # Compare the string with its reverse
    return s == s[::-1]