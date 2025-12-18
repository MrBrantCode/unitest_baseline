"""
QUESTION:
Write a function `validate_password(password)` that checks if a given password is valid. 

A password is considered valid if it meets the following conditions:
- It contains at least 16 characters.
- It contains at least two uppercase letters.
- It contains at least two lowercase letters.
- It contains at least two digits.
- It contains at least two special characters (!, @, #, $, %, ^, &, *).
- It does not contain any consecutive characters that are the same.
- It does not contain any consecutive characters that are in ascending or descending alphabetical order.
- It does not contain any consecutive characters that are in ascending or descending numerical order.
- It does not handle None or empty string inputs and returns False in such cases.

The function should not use any built-in functions or regular expressions to solve this problem.
"""

def validate_password(password):
    if password is None or password == "":
        return False
    if len(password) < 16:
        return False
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_char_count = 0
    prev_char = ""
    for char in password:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in "!@#$%^&*":
            special_char_count += 1
        if char == prev_char:
            return False
        if prev_char != "":
            if ord(char) - ord(prev_char) == 1 or ord(char) - ord(prev_char) == -1:
                return False
        prev_char = char
    if uppercase_count < 2 or lowercase_count < 2 or digit_count < 2 or special_char_count < 2:
        return False
    return True