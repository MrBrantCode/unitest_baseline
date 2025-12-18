"""
QUESTION:
Write a function `is_palindrome` that takes a string as input and returns True if the string is a palindrome (ignoring non-alphanumeric characters and case), and False otherwise. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def is_palindrome(s):
    # Remove all non-alphanumeric characters and convert to lowercase
    s = ''.join(filter(str.isalnum, s.lower()))
    
    # Check if the string is equal to its reverse
    return s == s[::-1]