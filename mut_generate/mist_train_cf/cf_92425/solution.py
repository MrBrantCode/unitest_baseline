"""
QUESTION:
Create a function `is_palindrome` that determines if a given string is a palindrome. The function should ignore non-alphanumeric characters, be case-insensitive, and return a boolean value indicating whether the input string is a palindrome or not.
"""

def is_palindrome(string):
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(filter(str.isalnum, string.lower()))
    # Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]