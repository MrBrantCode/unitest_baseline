"""
QUESTION:
Implement a function `is_palindrome(s)` that determines if a string `s` is a palindrome, considering only alphanumeric characters and ignoring case sensitivity, while ignoring any spaces or special characters. The time complexity of the solution should be O(n), where n is the length of the input string.
"""

def is_palindrome(s):
    # Remove spaces and special characters
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Check if the modified string is equal to its reverse
    return s == s[::-1]