"""
QUESTION:
Create a function named `remove_last_two_chars` that takes a string as input. The input string can be up to 100 characters long and may contain alphanumeric characters, special symbols like @, #, $, and %, as well as non-ASCII characters. The function should remove any leading or trailing whitespace characters and return the string without its last two letters. If the input string is longer than 100 characters or contains illegal characters like !, ?, or &, the function should return an error message instead.
"""

def remove_last_two_chars(string):
    # Check if string length is greater than 100
    if len(string) > 100:
        return "Input string is too long"

    # Check if string contains any illegal characters
    illegal_characters = ['!', '?', '&']
    if any(char in string for char in illegal_characters):
        return "Input string contains illegal characters"

    # Remove leading and trailing whitespace
    string = string.strip()

    # Remove last two characters
    string = string[:-2]

    return string