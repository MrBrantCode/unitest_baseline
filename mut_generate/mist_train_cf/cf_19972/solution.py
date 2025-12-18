"""
QUESTION:
Create a function named `reverse_and_remove_whitespace` that takes one string parameter. The function should reverse the input string, remove all white spaces from the string, and return the resulting string. The function must be case-sensitive and able to handle special characters. Additionally, create another function `is_palindrome` to check if the resulting string is a palindrome. Ensure that both functions can handle strings of any length and have an efficient time complexity of O(n).
"""

def reverse_and_remove_whitespace(s):
    """
    Reverses the input string and removes all white spaces.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The reversed and whitespace removed string.
    """
    return ''.join(char for char in reversed(s) if char != " ")


def is_palindrome(s):
    """
    Checks if the input string is a palindrome.
    
    Args:
    s (str): The input string.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]