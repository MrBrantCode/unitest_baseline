"""
QUESTION:
Write a function `longest_three_char_palindrome` that finds the longest substring of three characters in a given string that is a palindrome. The function should return the longest three-character palindromic substring if it exists, otherwise, return an empty string. The input string is guaranteed to be non-empty.
"""

def longest_three_char_palindrome(s):
    """
    Finds the longest substring of three characters in a given string that is a palindrome.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The longest three-character palindromic substring if it exists, otherwise an empty string.
    """
    longest_palindrome = ""
    for i in range(len(s) - 2):
        substr = s[i:i+3]
        if substr == substr[::-1] and len(substr) > len(longest_palindrome):
            longest_palindrome = substr
    return longest_palindrome