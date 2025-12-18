"""
QUESTION:
Create a function `is_valid_number` that takes a string as input and returns True if the string is at least 5 characters long, starts with a letter, ends with a digit, and has at least one special character in between, and False otherwise. The string should only contain digits, alphabetic characters, and special characters.
"""

def is_valid_number(string):
    if not string:
        return False

    if not (string[0].isalpha() and string[-1].isdigit()):
        return False

    special_char_count = 0
    for char in string[1:-1]:
        if not char.isalpha() and not char.isdigit():
            special_char_count += 1

    if special_char_count < 1 or len(string) < 5:
        return False

    return True