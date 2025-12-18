"""
QUESTION:
Create a function named `evaluate_password` that evaluates the strength of a given password and returns a classification of 'Poor', 'Average', or 'Strong'. The function should consider the length of the password and its complexity, including the presence of numbers, capital letters, and lowercase letters. The password should be classified as follows:
- 'Poor' if it's less than 6 characters long.
- 'Average' if it's 6-10 characters long and contains at least one number, one capital letter, and one lowercase letter.
- 'Strong' if it's more than 10 characters long.
"""

import re


def evaluate_password(password: str):
    """
    A simple password strength checker. Strength classified to Poor, Average, Strong
    """

    # Calculate password length and set strength to poor.
    length = len(password)
    strength = 'Poor'

    # Check length.
    if length < 6:
        return strength

    # Calculate strength of password.
    if (re.search(r'\d', password) is not None and    # contains numbers
            re.search(r'[A-Z]', password) is not None and    # contains capital letters
            re.search(r'[a-z]', password) is not None):  # contains lowercase letters
        strength = 'Average'

    if length > 10:
        strength = 'Strong'

    return strength