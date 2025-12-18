"""
QUESTION:
Create a function `create_palindrome(input_string)` that takes a string as input, removes non-alphabet characters, and converts it to lowercase. The function should then return a palindrome by concatenating the cleaned string with its reverse. Assume that palindromes are not case-sensitive and ignore non-alphabet characters.
"""

import re

def create_palindrome(input_string):
    # Convert to lower case
    input_string = input_string.lower()

    # Remove all non-alphabet characters
    cleaned_string = re.sub(r'[^a-z]', '', input_string)

    # Generate the palindrome by concatenating the cleaned string and its reverse
    palindrome = cleaned_string + cleaned_string[::-1]

    return palindrome