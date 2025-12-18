"""
QUESTION:
Write a function `find_longest_strings(strings)` that takes a list of strings as input. It should return the string(s) with the maximum length, excluding strings containing special characters or numbers. If multiple strings have the same maximum length, all of them should be returned. The maximum length of any individual string is 50 characters.
"""

def find_longest_strings(strings):
    """
    This function takes a list of strings as input and returns the string(s) with the maximum length.
    It excludes strings containing special characters or numbers. If multiple strings have the same maximum length, all of them are returned.

    Args:
        strings (list): A list of strings.

    Returns:
        list: A list of strings with the maximum length.
    """
    max_length = 0
    longest_strings = []

    for string in strings:
        if any(char.isdigit() or not char.isalnum() for char in string):
            continue
        if len(string) > max_length:
            max_length = len(string)
            longest_strings = [string]
        elif len(string) == max_length:
            longest_strings.append(string)

    return longest_strings