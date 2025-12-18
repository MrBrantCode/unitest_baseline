"""
QUESTION:
Create a function `is_valid_palindrome` that takes a string as input and returns `True` if the input string is a palindrome disregarding non-alphanumeric characters and case, and `False` otherwise. The function should ignore non-alphanumeric characters and be case-insensitive.
"""

def is_valid_palindrome(s: str) -> bool:
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the modified string is equal to its reverse
    return s == s[::-1]