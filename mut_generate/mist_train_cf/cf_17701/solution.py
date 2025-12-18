"""
QUESTION:
Write a function `remove_extra_spaces` that takes a string as input and returns the string with extra spaces removed and spaces made consistent, in uppercase. The input string can be of any length and can contain special characters. The function should remove leading and trailing spaces, replace consecutive spaces with a single space, and convert the string to uppercase. Note that this function should not handle the input length check; the input string is guaranteed to be at least 10 characters long.
"""

def remove_extra_spaces(string):
    # Remove leading and trailing spaces
    string = string.strip()

    # Replace consecutive spaces with a single space
    string = ' '.join(string.split())

    # Convert the string to uppercase
    string = string.upper()

    return string