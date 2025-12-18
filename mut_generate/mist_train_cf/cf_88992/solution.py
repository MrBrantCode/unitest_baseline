"""
QUESTION:
Create a function named `reverse_string` that takes a string `input_str` as input and returns a new string. The returned string should be in reverse order, but only if the input string contains at least one uppercase letter, one lowercase letter, one digit, and one special character. If the input string does not meet these conditions, return the original string. The function must have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

import string

def reverse_string(input_str):
    # Check if the string contains at least one uppercase letter, one lowercase letter, one digit, and one special character
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    for char in input_str:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True

        # If all the required characters are found, break the loop
        if has_uppercase and has_lowercase and has_digit and has_special:
            break

    # If any of the required characters is missing, return the original string
    if not (has_uppercase and has_lowercase and has_digit and has_special):
        return input_str

    # Reverse the string
    reversed_str = input_str[::-1]
    return reversed_str