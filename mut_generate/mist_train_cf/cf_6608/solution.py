"""
QUESTION:
Write a recursive function `is_palindrome` that checks if a given string is a palindrome without using extra space. The function should ignore case sensitivity and consider only alphanumeric characters, ignoring special characters and whitespace. The string may contain up to 1000 characters.
"""

def is_palindrome(s):
    # Base case: if the string is empty or has only one character, it is a palindrome
    if len(s) <= 1:
        return True
    
    # Check if the first and last characters are alphanumeric
    if not s[0].isalnum():
        return is_palindrome(s[1:])
    if not s[-1].isalnum():
        return is_palindrome(s[:-1])
    
    # Convert both characters to lowercase to ignore case sensitivity
    if s[0].lower() != s[-1].lower():
        return False
    
    # Recursively check if the string without the first and last characters is a palindrome
    return is_palindrome(s[1:-1])