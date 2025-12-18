"""
QUESTION:
Write a function `validate_password(password)` that takes a password as input and returns `True` if the password is valid and `False` otherwise. 

A password is considered valid if it meets the following criteria:
1. It contains at least 16 characters.
2. It contains at least two uppercase letters.
3. It contains at least two lowercase letters.
4. It contains at least two digits.
5. It contains at least two special characters (!, @, #, $, %, ^, &, *).
6. It does not contain any consecutive characters that are the same.
7. It does not contain any consecutive characters that are in ascending or descending alphabetical order.
8. It does not contain any consecutive characters that are in ascending or descending numerical order.

The function should also handle the case when the input password is `None` or an empty string, and return `False` in such cases. 

The function should not use any built-in functions or regular expressions to solve this problem.
"""

def entrance(password):
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
        if ord('A') <= ord(char) <= ord('Z'):
            uppercase_count += 1
        elif ord('a') <= ord(char) <= ord('z'):
            lowercase_count += 1
        elif ord('0') <= ord(char) <= ord('9'):
            digit_count += 1
        elif char in "!@#$%^&*":
            special_char_count += 1
        if char == prev_char:
            return False
        if prev_char != "":
            if ord(char) - ord(prev_char) == 1 or ord(char) - ord(prev_char) == -1:
                if (ord('a') <= ord(char) <= ord('z') and ord('a') <= ord(prev_char) <= ord('z')) or (ord('A') <= ord(char) <= ord('Z') and ord('A') <= ord(prev_char) <= ord('Z')) or (ord('0') <= ord(char) <= ord('9') and ord('0') <= ord(prev_char) <= ord('9')):
                    return False
        prev_char = char
    if uppercase_count < 2 or lowercase_count < 2 or digit_count < 2 or special_char_count < 2:
        return False
    return True