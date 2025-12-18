"""
QUESTION:
Create a function `check_string` that takes one argument, a string. The function should return the number of uppercase letters in the string if it contains at least one uppercase letter, one lowercase letter, and one numeric digit. Otherwise, it should return False.
"""

def entrance(s):
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    uppercase_count = 0

    for char in s:
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