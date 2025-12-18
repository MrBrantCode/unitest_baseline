"""
QUESTION:
Write a function `longestPalindrome` that takes a list of strings as input and returns the longest palindromic string. If there are multiple longest palindromic strings, return the first one encountered. If no palindromes exist in the list, return `Optional.empty`.
"""

def longest_palindrome(strings):
    """
    This function takes a list of strings as input and returns the longest palindromic string.
    If there are multiple longest palindromic strings, return the first one encountered.
    If no palindromes exist in the list, return None.

    Args:
        strings (list): A list of strings

    Returns:
        str or None: The longest palindromic string or None if no palindromes exist
    """

    def is_palindrome(s):
        """
        Helper function to check if a string is a palindrome

        Args:
            s (str): The string to check

        Returns:
            bool: True if the string is a palindrome, False otherwise
        """
        return s == s[::-1]

    return max((s for s in strings if is_palindrome(s)), default=None, key=len)