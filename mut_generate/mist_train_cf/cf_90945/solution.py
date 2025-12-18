"""
QUESTION:
Write a function named `is_palindrome` that takes a string `s` as input. The function should return `True` if the string is a palindrome and `False` otherwise. The function should ignore any non-alphanumeric characters and treat uppercase and lowercase letters as equivalent. A palindrome is a sequence of characters that reads the same forward and backward.
"""

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]