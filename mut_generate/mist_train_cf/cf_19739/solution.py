"""
QUESTION:
Write a function `isPalindrome` that checks if a given string is a palindrome. The function should ignore special characters and whitespace, be case-insensitive, and have a time complexity of O(n) and a space complexity of O(1).
"""

def isPalindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome. The function ignores special characters and whitespace, 
    is case-insensitive, and has a time complexity of O(n) and a space complexity of O(1).

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left, right = left + 1, right - 1
    return True