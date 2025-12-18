"""
QUESTION:
Create a function called `is_palindrome_string` that takes an input string `s` and returns `True` if the string is a palindrome, ignoring non-alphabetic characters and considering both uppercase and lowercase letters, and `False` otherwise. The function must have a time complexity of O(n), where n is the length of the input string, and cannot use any built-in string manipulation functions or data structures.
"""

def is_palindrome_string(s, start=None, end=None):
    """
    Checks if the input string is a palindrome, ignoring non-alphabetic characters 
    and considering both uppercase and lowercase letters.

    Args:
        s (str): The input string.
        start (int): The starting index of the substring to check (default: None).
        end (int): The ending index of the substring to check (default: None).

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    
    # Initialize start and end pointers if not provided
    if start is None:
        start = 0
    if end is None:
        end = len(s) - 1

    # Base case: if start and end pointers cross each other, it is a palindrome
    if start >= end:
        return True
    
    # Check if the characters at start and end positions are valid alphabetic characters
    if not s[start].isalpha():
        return is_palindrome_string(s, start + 1, end)
    if not s[end].isalpha():
        return is_palindrome_string(s, start, end - 1)
    
    # Compare the characters at start and end positions, ignoring case
    if s[start].lower() != s[end].lower():
        return False
    
    # Recursively check the remaining substring by moving start and end pointers
    return is_palindrome_string(s, start + 1, end - 1)