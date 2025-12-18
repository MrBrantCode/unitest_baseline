"""
QUESTION:
Implement a function `is_palindrome(s: str) -> bool` that checks whether a given string is a palindrome or not, ignoring non-alphanumeric characters and case. The function should return `True` if the input string is a palindrome and `False` otherwise. Assume the input string contains no spaces and may contain alphanumeric characters and punctuation.
"""

def entance(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char for char in s if char.isalnum()).lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]