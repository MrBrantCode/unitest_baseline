"""
QUESTION:
Create a function `perfect_palindrome(input_string)` that determines whether a given alphanumeric string is a palindrome, ignoring case, spaces, and special characters. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

def perfect_palindrome(input_string):
    # Removing spaces and converting to lower case
    input_string = input_string.replace(" ", "").lower()

    # Removing special symbols or punctuation
    input_string = ''.join(e for e in input_string if e.isalnum())

    # Checking if the string is palindrome
    is_palindrome = input_string == input_string[::-1]

    return is_palindrome