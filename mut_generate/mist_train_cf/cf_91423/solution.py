"""
QUESTION:
Write a function `is_palindrome(s)` that determines if the alphanumeric characters in a given string form a palindrome, ignoring case, spaces, and special characters. The function should return `True` if the string is a palindrome and `False` otherwise. The time complexity of the solution should be O(n), where n is the length of the input string.
"""

def entance(s):
    # Remove all non-alphanumeric characters and convert to lowercase
    s = ''.join(filter(str.isalnum, s.lower()))
    
    # Check if the string is equal to its reverse
    return s == s[::-1]