"""
QUESTION:
Create a function `is_palindrome(s)` that determines whether a given string is a palindrome, ignoring spaces, punctuation, and capitalization. The function should return `True` if the string is a palindrome and `False` otherwise, with a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

def is_palindrome(s):
    # Convert the string to lowercase and remove spaces and punctuation
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    
    # Check if the modified string is equal to its reverse
    return s == s[::-1]