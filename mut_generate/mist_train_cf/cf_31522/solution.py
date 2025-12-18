"""
QUESTION:
Write a function `isPalindrome` that takes a string as input and returns `True` if the input string is a palindrome disregarding spaces, punctuation, and capitalization, and `False` otherwise.
"""

def isPalindrome(s: str) -> bool:
    # Remove spaces and punctuation and convert to lowercase
    clean_str = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the clean string is equal to its reverse
    return clean_str == clean_str[::-1]