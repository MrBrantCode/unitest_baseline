"""
QUESTION:
Implement a Python function named `is_palindrome` that checks if a given string is a palindrome. The function should disregard spaces, punctuation, and capitalization. It should also handle multiple lines, non-alphanumeric characters, Unicode characters, and large input strings efficiently. The function should return True if the input string is a palindrome and False otherwise. The function should not use any built-in Python functions or methods that directly solve this problem.
"""

def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome, disregarding spaces, punctuation, and capitalization.
    
    Args:
    s (str): The input string to check.
    
    Returns:
    bool: True if the input string is a palindrome, False otherwise.
    """

    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())

    # Initialize two pointers, one at the start and one at the end of the string
    left = 0
    right = len(s) - 1

    # Compare characters from the start and end, moving towards the center
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    # If the loop completes without finding a mismatch, the string is a palindrome
    return True