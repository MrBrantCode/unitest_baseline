"""
QUESTION:
Implement the `is_palindrome` function to determine whether a given string is a palindrome, disregarding spaces, punctuation, and capitalization. The function should take a single string parameter `s` containing only alphanumeric characters and spaces, and return `True` if the input string is a palindrome and `False` otherwise.
"""

def is_palindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(c for c in s if c.isalnum()).lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]