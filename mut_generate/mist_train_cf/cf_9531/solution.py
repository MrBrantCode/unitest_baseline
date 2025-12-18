"""
QUESTION:
Create a function called `is_palindrome` that takes a string as input and returns a boolean indicating whether the string is a palindrome, ignoring non-alphanumeric characters and treating uppercase and lowercase letters as equivalent.
"""

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]