"""
QUESTION:
Create a function `check_palindrome_and_case` that takes a string as input. The function should return True if the input string is a palindrome and contains at least one uppercase letter, and False otherwise. The palindrome check should be case-insensitive and ignore non-alphanumeric characters.
"""

def check_palindrome_and_case(s: str) -> bool:
    """
    Checks if the input string is a palindrome and contains at least one uppercase letter.
    
    The palindrome check is case-insensitive and ignores non-alphanumeric characters.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    bool: True if the string is a palindrome and contains at least one uppercase letter, False otherwise.
    """
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1] and any(char.isupper() for char in s)