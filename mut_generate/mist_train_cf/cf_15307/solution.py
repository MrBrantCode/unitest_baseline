"""
QUESTION:
Create a function `check_string(input_string)` that checks if a given string contains at least one uppercase letter, one lowercase letter, and one numeric digit. The function should return the number of uppercase letters found in the string if all conditions are met; otherwise, it should return -1. The input string may contain special characters.
"""

def check_string(input_string):
    uppercase_count = 0
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if has_uppercase and has_lowercase and has_digit:
        return uppercase_count
    else:
        return -1