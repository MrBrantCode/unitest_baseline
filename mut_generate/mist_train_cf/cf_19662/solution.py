"""
QUESTION:
Implement a function `is_palindrome(s)` that takes a string `s` as input and returns `True` if the string is a palindrome and `False` otherwise. The function should be case-insensitive, ignore non-alphanumeric characters, and handle Unicode characters. If the input string contains multiple lines, each line should be considered as a separate word and the function should return `True` only if all words are palindromes. The implementation should not use any built-in Python functions or methods that directly solve this problem.
"""

def is_palindrome(s):
    # Remove non-alphanumeric characters
    s = ''.join(c for c in s if c.isalnum())
    
    # Convert string to lowercase
    s = s.lower()
    
    # Check if each word is a palindrome
    words = s.split()
    for word in words:
        if word != word[::-1]:
            return False
    
    return True