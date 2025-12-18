"""
QUESTION:
Create a function `password_strength` that determines the strength of a given password based on its length, inclusion of numbers, special characters, uppercase, and lowercase letters. The function should return one of the following categories: 'Password cannot be blank', 'Very weak', 'Weak', 'Medium', 'Strong', 'Very strong'. The password strength is evaluated using the following criteria: a score is assigned based on the length of the password, presence of digits, presence of both lowercase and uppercase letters, and presence of special characters.
"""

import re

def password_strength(password):
    strength = ['Password cannot be blank', 'Very weak', 'Weak', 'Medium', 'Strong', 'Very strong']
    score = 1

    if len(password) < 1:
        return strength[0]

    if len(password) < 4:
        return strength[1]

    if len(password) >= 8:
        score += 1

    if re.search("[0-9]", password):
        score += 1

    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1

    if re.search("[^A-Za-z0-9]", password):
        score += 1

    return strength[min(score, len(strength) - 1)]