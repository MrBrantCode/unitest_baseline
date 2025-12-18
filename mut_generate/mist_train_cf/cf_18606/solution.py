"""
QUESTION:
Create a function `is_palindrome(str1, str2)` to determine if a given string `str1` is a palindrome of another string `str2`, ignoring spaces, punctuation, and capitalization. The function should handle strings with special characters or non-alphabetic characters and should be efficient for inputs up to 1 million characters.
"""

def is_palindrome(str1, str2):
    # Convert the strings to lowercase and remove spaces and punctuation
    str1 = ''.join(c.lower() for c in str1 if c.isalnum())
    str2 = ''.join(c.lower() for c in str2 if c.isalnum())

    # Check if the reversed string is equal to the original string
    return str1 == str2[::-1]