"""
QUESTION:
Create a function `count_chars_in_palindrome(s)` that takes a string `s` as input and returns the frequency of each character in `s` if `s` is a palindrome, ignoring spacing and punctuation. The function should handle Unicode characters and be efficient for large strings.
"""

from collections import Counter

def count_chars_in_palindrome(s):
    """
    Returns the frequency of each character in string `s` if `s` is a palindrome, 
    ignoring spacing and punctuation.

    Args:
        s (str): Input string

    Returns:
        Counter: Frequency of each character in `s` if `s` is a palindrome
    """
    s = ''.join(c for c in s if c.isalpha()).lower()
    if s == s[::-1]:
        return Counter(s)
    else:
        return None