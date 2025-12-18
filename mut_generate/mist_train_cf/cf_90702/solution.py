"""
QUESTION:
Create a function `check_string` that takes a string as an argument and checks if it contains at least one uppercase letter, one lowercase letter, and one numeric digit. The function should return the number of uppercase letters found in the string if the conditions are met; otherwise, it should return False.
"""

def check_string(string):
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    uppercase_count = 0

    for char in string:
        if char.isupper():
            has_uppercase = True
            uppercase_count += 1
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if has_uppercase and has_lowercase and has_digit:
        return uppercase_count
    else:
        return False