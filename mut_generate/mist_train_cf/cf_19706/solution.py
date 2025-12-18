"""
QUESTION:
Write a function named `is_palindrome` that determines whether a given string is a palindrome, considering case sensitivity and ignoring any special characters or spaces. The function should take one string as input and return a boolean value indicating whether the string is a palindrome.
"""

def is_palindrome(s):
    """
    This function checks whether a given string is a palindrome, 
    considering case sensitivity and ignoring any special characters or spaces.
    
    Parameters:
    s (str): The input string to be checked.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Compare the string with its reverse
    return s == s[::-1]