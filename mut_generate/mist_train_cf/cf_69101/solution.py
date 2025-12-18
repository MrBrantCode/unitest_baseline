"""
QUESTION:
Create a function named `analyze_password` that takes one argument `password` and returns a string indicating the strength of the password and a dictionary containing the password's complexity. The function should check if the password meets the following conditions:

- The length of the password is at least 8 characters.
- The password contains at least one digit.
- The password contains at least one uppercase letter.
- The password contains at least one lowercase letter.
- The password contains at least one symbol (non-alphanumeric character).

The function should return a string indicating whether the password is strong enough and a dictionary with boolean values for each complexity condition.
"""

import re

def analyze_password(password):
    """
    Analyze the complexity of the given password
    """
    # calculate the length
    length_error = len(password) < 8

    # check for digits
    digit_error = re.search(r"\d", password) is None

    # check for uppercase 
    uppercase_error = re.search(r"[A-Z]", password) is None

    # check for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # check for symbols
    symbol_error = re.search(r"\W", password) is None

    # compile overall error variable
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )

    # show result
    password_strength = "Your password is {0}strong enough.".format("" if password_ok else "not ")

    complexity = {
        'length_error': length_error,
        'digit_error': digit_error,
        'uppercase_error': uppercase_error,
        'lowercase_error': lowercase_error,
        'symbol_error': symbol_error,
    }

    return password_strength, complexity