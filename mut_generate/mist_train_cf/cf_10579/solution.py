"""
QUESTION:
Write a function named `is_palindrome` that takes a string as input, checks if it's a palindrome when ignoring non-alphanumeric characters and case, and returns a boolean value. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome when ignoring non-alphanumeric characters and case.
    
    Time complexity: O(n)
    Space complexity: O(n)
    
    Args:
    s (str): The input string.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    
    # initialize two pointers
    left = 0
    right = len(s) - 1

    # iterate until the two pointers meet or cross each other
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True