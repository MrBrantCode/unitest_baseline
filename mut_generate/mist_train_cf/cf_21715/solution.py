"""
QUESTION:
Write a function `is_palindrome(string)` that checks whether a given string is a palindrome, ignoring spaces, punctuation marks, and capitalization. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.
"""

def is_palindrome(string):
    # Convert the string to lowercase and remove spaces and punctuation
    string = ''.join(c.lower() for c in string if c.isalnum())

    # Check if the string is a palindrome by comparing it with its reverse
    return string == string[::-1]