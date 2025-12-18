"""
QUESTION:
Implement a function `is_palindrome(s)` that checks if the given string `s` is a palindrome. The function should not use any built-in string manipulation functions and should have a time complexity of O(n), where n is the length of the string. The function should return a boolean value indicating whether the string is a palindrome or not.
"""

def entrance(s):
    """
    Check if the given string is a palindrome.
    
    Parameters:
    s (str): The string to be checked.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True