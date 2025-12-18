"""
QUESTION:
Implement the `is_palindrome(s)` function to determine if a given string `s` is a palindrome. A palindrome is a string that reads the same forwards and backwards.

The function `is_palindrome` takes a single string parameter `s` of length between 1 and 10^5, consisting of lowercase and/or uppercase letters, spaces, and/or punctuation marks. The function should return `True` if `s` is a palindrome and `False` otherwise.
"""

def is_palindrome(s):
    """
    This function determines if a given string is a palindrome.
    
    Parameters:
    s (str): The input string to be checked.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    
    # Convert the string to lowercase and remove any spaces or punctuation marks
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Initialize two pointers, one starting from the beginning and one from the end of the string
    left, right = 0, len(s) - 1
    
    # Compare characters from the start and end of the string and move towards the middle
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    # If the loop completes without finding any unequal characters, the string is a palindrome
    return True