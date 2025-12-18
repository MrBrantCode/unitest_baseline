"""
QUESTION:
Write a function `isPalindrome` that checks if a given string is a palindrome with a time complexity of O(n) and a space complexity of O(1). The function should return `true` if the string is a palindrome and `false` otherwise.
"""

def isPalindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True