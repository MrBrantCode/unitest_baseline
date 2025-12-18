"""
QUESTION:
Create a function named `password_strength` that takes one string argument `password`. The function should evaluate the reliability of the password based on the following criteria:
- The password length is at least 8 characters.
- The password contains at least one uppercase letter.
- The password contains at least one lowercase letter.
- The password contains at least one digit.
- The password contains at least one special character.

The function should return a dictionary with boolean values indicating whether the password meets each of the above criteria and an 'Password valid' key that indicates whether the password meets all the criteria.
"""

import re

def password_strength(password):
    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"\W", password) is None

    # overall result
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )

    password_strength = {
        'Password valid' : password_ok,
        'Length >= 8' : not length_error,
        'Contains digits' : not digit_error,
        'Contains uppercase' : not uppercase_error,
        'Contains lowercase' : not lowercase_error,
        'Contains symbols' : not symbol_error,
    }

    return password_strength