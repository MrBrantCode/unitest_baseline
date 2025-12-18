"""
QUESTION:
Create a function `is_palindrome` that takes a string input. The function must return `True` if the input string, after removing spaces and special characters, and converting to lowercase, reads the same forwards and backwards, and `False` otherwise.
"""

def is_palindrome(input_string):
    # Remove spaces, convert to lower case and ignore special characters.
    alpha_numeric_chars = [char for char in input_string.lower() if char.isalnum()]
    cleaned_input = ''.join(alpha_numeric_chars)

    # Check if the string is the same read forwards and backwards.
    return cleaned_input == cleaned_input[::-1]